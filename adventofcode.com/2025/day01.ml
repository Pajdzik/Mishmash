let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'
  |> List.filter (fun x -> x <> "")


let process lines =
  let rec process_lines lines count position =
    match lines with
    | [] -> count
    | instruction :: rest ->
        let direction = String.get instruction 0 in
        let distance = int_of_string (String.sub instruction 1 (String.length instruction - 1)) in
        let new_position = match direction with
          | 'R' -> (position + distance)
          | 'L' -> (position - distance)
          | _ -> failwith "Invalid direction"
        in

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
        process_lines rest new_count capped_position
  in
  process_lines lines 0 50

let () =
  read_lines "day01.txt" |> process |> print_int;
  print_newline ()
