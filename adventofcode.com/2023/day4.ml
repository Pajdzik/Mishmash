let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'

let print_string_list arr = List.iter print_string arr

let rec power base exponent =
  match exponent with 0 -> 1 | n -> base * power base (n - 1)

let process_line line =
  let extract_scratch_card_data line =
    let parse_numbers_to_array str =
      String.trim str |> String.split_on_char ' '
      |> List.filter (fun c -> not (String.equal c String.empty))
      |> List.map (fun d ->
             print_int (String.length d);
             print_string (" d: '" ^ d ^ "'\n");
             int_of_string d)
    in

    let extract_numbers numbers_str =
      let scratch_card_numbers = String.split_on_char '|' numbers_str in
      match scratch_card_numbers with
      | [ winning; owned ] ->
          (parse_numbers_to_array winning, parse_numbers_to_array owned)
      | _ -> ([], [])
    in

    let scratch_card_data = String.split_on_char ':' line in
    match scratch_card_data with
    | [ _; numbers_data ] -> extract_numbers numbers_data
    | _ -> ([], [])
  in

  let winning_numbers, owned_numbers = extract_scratch_card_data line in
  let overlap =
    List.filter (fun el -> List.mem el winning_numbers) owned_numbers
  in
  let ovelap_count = List.length overlap in
  match ovelap_count with 0 -> 0 | n -> power 2 (n - 1)

let process_part1 lines =
  let wins = List.map process_line lines in
  List.fold_left ( + ) 0 wins

let () = process_part1 (read_lines "day4.txt") |> print_int
