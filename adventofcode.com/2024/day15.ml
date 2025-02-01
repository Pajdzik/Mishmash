let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'

type status = Wall | Robot | Box | Space
type direction = Up | Down | Left | Right
type map = status array array
type input = { map : map; directions : direction list }

let print_map map (robot_x, robot_y) =
  Array.iteri
    (fun x row ->
      Array.iteri
        (fun y status ->
          let c =
            if y = robot_y && x = robot_x then '@'
            else
              match status with
              | Wall -> '#'
              | Box -> 'O'
              | Space -> '.'
              | _ -> failwith "Unexpected status when printing"
          in
          Printf.printf "%c" c)
        row;
      print_newline ())
    map;
  print_newline ()

let parse_input (lines : string list) =
  let parse_status c =
    match c with
    | '#' -> Wall
    | '@' -> Robot
    | 'O' -> Box
    | '.' -> Space
    | c -> failwith ("Unrecognized status: " ^ String.make 1 c)
  in

  let rec parse_map map lines =
    match lines with
    | [] -> failwith "Input ended too soon"
    | line :: rest -> (
        match line with
        | "" -> (map, rest)
        | _ ->
            let status_line =
              String.to_seq line |> Seq.map parse_status |> Array.of_seq
            in
            parse_map (Array.append map [| status_line |]) rest)
  in

  let parse_direction c =
    match c with
    | '^' -> Up
    | 'v' -> Down
    | '<' -> Left
    | '>' -> Right
    | c -> failwith ("Unrecognized direction: " ^ String.make 1 c)
  in

  let rec parse_directions directions lines =
    match lines with
    | [] -> directions
    | line :: rest ->
        let direction_line =
          line |> String.to_seq |> Seq.map parse_direction |> List.of_seq
        in
        parse_directions (directions @ direction_line) rest
  in

  let map, direction_lines = parse_map [||] lines in
  let directions = parse_directions [] direction_lines in
  { map; directions }

let print_move direction =
  print_endline
    ("Move: "
    ^
    match direction with Up -> "^" | Down -> "v" | Left -> "<" | Right -> ">")

let process lines =
  let find_starting_point map =
    let find_starting_point_in_a_row row_index =
      Array.find_index (fun x -> x = Robot) map.(row_index)
    in

    let rec find_starting_point' row_index =
      let col_index = find_starting_point_in_a_row row_index in
      match col_index with
      | None -> find_starting_point' (row_index + 1)
      | Some col_index -> (row_index, col_index)
    in

    find_starting_point' 0
  in

  let process_moves input starting_point =
    let get_next_position (x, y) direction =
      match direction with
      | Up -> (x - 1, y)
      | Down -> (x + 1, y)
      | Left -> (x, y - 1)
      | Right -> (x, y + 1)
    in

    let move_box_to_the_next_available_space map direction box_position =
      let rec find_next_box_position' box_position =
        let space_behind_the_box_position =
          get_next_position box_position direction
        in
        let x, y = box_position in
        match map.(x).(y) with
        | Wall -> None
        | Space -> Some box_position
        | Box -> find_next_box_position' space_behind_the_box_position
        | _ -> failwith "Unexpected status when finding next box position"
      in

      let new_box_position = find_next_box_position' box_position in
      match new_box_position with
      | None -> false
      | Some new_box_position ->
          map.(fst box_position).(snd box_position) <- Space;
          map.(fst new_box_position).(snd new_box_position) <- Box;
          true
    in

    let rec process_moves' map directions robot_position =
      (* Printf.printf "Robot position %d, %d\n" (fst robot_position)
        (snd robot_position); *)
      match directions with
      | [] -> map
      | direction :: rest ->
          let new_x, new_y = get_next_position robot_position direction in
          let next_field_status = map.(new_x).(new_y) in
(* 
          print_move direction;
          print_map map robot_position; *)

          let next_robot_position =
            match next_field_status with
            | Wall -> robot_position
            | Space -> (new_x, new_y)
            | Robot -> failwith "Robot hit another robot"
            | Box ->
                let managed_to_move =
                  move_box_to_the_next_available_space map direction
                    (new_x, new_y)
                in
                if managed_to_move then (new_x, new_y) else robot_position
          in

          (* Printf.printf "Next robot position %d, %d\n\n\n" (fst next_robot_position)
            (snd next_robot_position); *)

          process_moves' map rest next_robot_position
    in

    let rec sum_positions map acc row_index =
      if row_index = Array.length map then acc
      else
        let row = map.(row_index) in
        let rec sum_positions_in_row acc col_index =
          if col_index = Array.length row then acc
          else
            let status = row.(col_index) in
            let position_value =
              match status with Box -> (row_index * 100) + col_index | _ -> 0
            in
            sum_positions_in_row (acc + position_value) (col_index + 1)
        in

        sum_positions map (sum_positions_in_row acc 0) (row_index + 1)
    in

    let map = input.map in
    map.(fst starting_point).(snd starting_point) <- Space;
    let processed_map = process_moves' map input.directions starting_point in
    print_map processed_map starting_point;
    sum_positions processed_map 0 0
  in

  let input = parse_input lines in
  let starting_point = find_starting_point input.map in
  Printf.printf "Starting point found: %d, %d\n" (fst starting_point)
    (snd starting_point);
  process_moves input starting_point

let () =
  read_lines "day15.txt" |> process |> print_int;
  print_newline ()
