let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'
  |> List.filter (fun x -> x <> "")

type memory_state = Active | Visited | Corrupted

let process lines =
  let parse_input (lines : string list) =
    lines
    |> List.map (String.split_on_char ',')
    |> List.map (fun a ->
           (int_of_string (List.nth a 0), int_of_string (List.nth a 1)))
  in

  let truncate_input input limit =
    let rec truncate_input' input' limit' acc =
      match limit' with
      | 0 -> acc
      | _ ->
          let x, y = List.hd input' in
          truncate_input' (List.tl input') (limit' - 1) ((x, y) :: acc)
      in

    List.rev (truncate_input' input limit [])
    in

  let create_map (corrupted_memory : (int * int) list) size =
    let map = Hashtbl.create ((size + 1) * (size + 1)) in
    List.iter (fun (x, y) -> Hashtbl.add map (y, x) Corrupted) corrupted_memory;

    map
  in

  let find_path_length map size =
    let to_explore = Queue.create () in
    Queue.push (0, 0, 0) to_explore;

    let rec try_find_path () =
      if Queue.is_empty to_explore then None
      else
        let node = Queue.pop to_explore in
        explore_node node
    and explore_node node =
      let x, y, p = node in
      if not (x >= 0 && y >= 0 && x < size && y < size) then try_find_path ()
      else
        let status = Hashtbl.find_opt map (x, y) in
        match status with
        | None ->
            if x == size - 1 && y == size - 1 then Some p
            else (
              print_string
                (Printf.sprintf "Exploring node: %d, %d, %d... " x y p);
              print_endline "Active";
              Hashtbl.add map (x, y) Visited;
              let children =
                [
                  (x + 1, y, p + 1);
                  (x - 1, y, p + 1);
                  (x, y + 1, p + 1);
                  (x, y - 1, p + 1);
                ]
              in
              List.iter (fun child -> Queue.push child to_explore) children;
              try_find_path ())
        | _ -> try_find_path ()
    in
    try_find_path ()
  in

  let print_map map size =
    for i = 0 to size - 1 do
      for j = 0 to size - 1 do
        match Hashtbl.find_opt map (i, j) with
        | None -> print_string "."
        | Some Active -> failwith "Active memory should not be printed"
        | Some Visited -> failwith "Visited memory should not be printed"
        | Some Corrupted -> print_string "#"
      done;
      print_newline ()
    done
  in


  let size = 71 in
  let input = truncate_input (parse_input lines) 1024 in
  let map = create_map input size in
  print_map map size;

  let result = find_path_length map size in
  match result with Some p -> p | None -> failwith "No path found"

let () =
  read_lines "day18.txt" |> process |> print_int;
  print_newline ()
