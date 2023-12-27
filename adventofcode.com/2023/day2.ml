let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all 
  |> String.split_on_char '\n'

let process_part1 input_lines = 
  let parse_line line = 
    let parse_id str = 
      (* "Game 1" *)
      let parts = String.split_on_char ' ' str in
      match parts with
      | [_; id] -> int_of_string id
      | _ -> failwith "No id" in

    let parse_games str =
      let parse_game game_str =
        let check_for_color str =
          (* "4 red" *)
          match String.split_on_char ' ' (String.trim str) with
          | [count; "red"] -> int_of_string count <= 12
          | [count; "green"] -> int_of_string count <= 13
          | [count; "blue"] -> int_of_string count <= 14
          | game -> failwith ("Unparsable colors: " ^ "'" ^ str ^ "'") in

        (* "3 blue, 4 red" *)
        let parts = String.split_on_char ',' game_str in
        List.for_all check_for_color parts in

      (* "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green" *)
      let game_parts = String.split_on_char ';' str in
      List.for_all parse_game game_parts in

    (* "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green" *)
    let parts = String.split_on_char ':' line in
    match parts with 
    | [id_part; games_part] -> (parse_id id_part, parse_games games_part)
    | _ -> (0, true)
   in

  let process_line line =
    match line with
    | "" -> (0, false)
    | line when String.starts_with line ~prefix:"Game" -> parse_line(line)
    | line -> failwith ("Unexpected line: " ^ line) in

  let results = List.map process_line input_lines in
  let positive_results = List.filter (fun (id, result) -> result = true) results in
  let ids = List.map (fun (id, _) -> id) positive_results in
  let sum = List.fold_left (+) 0 ids in
  sum

let () =
  read_lines "day2.txt"
  |> process_part1
  |> print_int