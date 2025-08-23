let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'

type field = Wall | Space | Start | End | Visited | Unknown

let print_map map =
  Array.iteri
    (fun x row ->
      Array.iteri
        (fun y field ->
          let c =
            match field with
            | Wall -> '#'
            | Space -> '.'
            | Start -> 'S'
            | End -> 'E'
            | Visited -> 'X'
            | Unknown -> '?'
          in
          Printf.printf "%c" c)
        row;
      print_newline ())
    map;
  print_newline ()

let parse_input (lines : string list) =
  let map_char c =
    match c with
    | '#' -> Wall
    | '.' -> Space
    | 'S' -> Start
    | 'E' -> End
    | _ -> failwith ("Unrecognized character: " ^ String.make 1 c)
  in

  let parse_line line =
    line |> String.to_seq |> Seq.map map_char |> Array.of_seq
  in

  let map = Array.make_matrix (List.length lines) 0 Unknown in

  let rec parse_input' map' lines row =
    match lines with
    | [] -> map
    | line :: rest ->
        let line' = parse_line line in
        map'.(row) <- line';
        parse_input' map' rest (row + 1)
  in

  parse_input' map lines 0

let process lines =
  let find_path_cost map =
    let rec find_start map' row col =
      if row >= Array.length map' then failwith "No start found"
      else
        let line = map'.(row) in
        if col >= Array.length line then find_start map' (row + 1) 0
        else
          match line.(col) with
          | Start -> (row, col)
          | _ -> find_start map' row (col + 1)
    in

    let get_new_cost cost last_dir dir =
      match last_dir = dir with true -> cost + 1 | false -> cost + 1001
    in

    let traverse map' start =
      let directions = [ (-1, 0); (0, 1); (1, 0); (0, -1) ] in
      let queue = Queue.create () in
      Queue.add (start, 0, (0, 1)) queue;

      let rec traverse' map'' =
        if Queue.is_empty queue then None
        else
          let pos, cost, dir = Queue.pop queue in
          Printf.printf "Position: (%d, %d)\tDirection (%d, %d)\tCost: %d\n"
            (fst pos) (snd pos) (fst dir) (snd dir) cost;
          print_map map'';
          print_endline "--------------------------------";
          let row, col = pos in
          match row >= Array.length map'' || col >= Array.length map''.(0) with
          | true -> None
          | _ -> (
              match map''.(row).(col) with
              | End ->
                  (* print_endline ("FOUND END!!! " ^ string_of_int cost);
                print_map map''; *)
                  Some cost
              | Visited -> None
              | Wall -> None
              | _ ->
                  let try_direction direction =
                    let dr, dc = direction in
                    let new_cost = get_new_cost cost dir direction in
                    let new_position = (row + dr, col + dc) in
                    traverse' map''
                  in
                  map''.(row).(col) <- Visited;

                  let n_cost = try_direction (-1, 0) in
                  let e_cost = try_direction (0, 1) in
                  let s_cost = try_direction (1, 0) in
                  let w_cost = try_direction (0, -1) in

                  let defined_costs =
                    List.filter_map Fun.id [ n_cost; e_cost; s_cost; w_cost ]
                  in
                  let min_cost = List.fold_left min max_int defined_costs in

                  map''.(row).(col) <- Space;
                  Some min_cost)
      in

      traverse' map' 0 (0, 1) start
    in

    let start = find_start map 0 0 in
    let result = traverse map start in
    match result with None -> failwith "No path found" | Some cost -> cost
  in
  parse_input lines |> find_path_cost

let () =
  read_lines "day16.test.txt" |> process |> print_int;
  print_newline ()
