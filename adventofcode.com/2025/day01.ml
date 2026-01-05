let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'
  |> List.filter (fun x -> x <> "")


let process lines =
  let parse_line line =
    let direction = String.get line 0 in
    let distance = int_of_string (String.sub line 1 (String.length line - 1)) in
    (direction, distance)
  in

  let get_new_position position direction distance =
    match direction with
    | 'R' -> position + distance
    | 'L' -> position - distance
    | _ -> failwith "Invalid direction"
  in

  let rec process_part2 lines count position =
    match lines with
    | [] -> count
    | instruction :: rest ->
        let (direction, distance) = parse_line instruction in
        let new_position = get_new_position position direction distance in

        let capped_position = match (new_position mod 100) with
          | p when p < 0 -> (100 + p)
          | p when p >= 100 -> (p - 100)
          | p -> p
        in
        
        let flip_position = get_new_position position direction (distance mod 100) in
        let flipped = ((flip_position <= 0 || flip_position >= 100) && position > 0) in
        let flip_addon = if flipped then 1 else 0 in

        let new_count = (distance / 100) + flip_addon + count in
        
        print_string (Printf.sprintf "Position: %d\t|\t" position);
        print_string (Printf.sprintf "Instruction:  %s\t|\t" instruction);
        print_string (Printf.sprintf "New Position:  %d\t|\t" new_position);
        print_string (Printf.sprintf "Cap Position:  %d\t|\t" capped_position);
        print_string (Printf.sprintf "Count: %d\t|\t" new_count);
        print_newline ();

        process_part2 rest new_count capped_position
  in

  let rec _process_part1 lines count position =
    match lines with
    | [] -> count
    | instruction :: rest ->
        let (direction, distance) = parse_line instruction in
        let new_position = get_new_position position direction distance in

        let capped_position = match (new_position mod 100) with
          | p when p < 0 -> (100 + p)
          | p when p >= 100 -> (p - 100)
          | p -> p
        in

        let new_count = match capped_position with
          | 0 -> count + 1
          | _ -> count
        in

        print_endline (Printf.sprintf "OG Position: %d, New Position: %d, Instruction: %s, Cap Position: %d" position new_position instruction capped_position);
        _process_part1 rest new_count capped_position
  in
  process_part2 lines 0 50

let () =
  read_lines "day01.txt" |> process |> print_int;
  print_newline ()
