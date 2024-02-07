let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'

let print_int_list arr = List.iter print_int arr
let print_string_list arr = List.iter print_string arr

let rec power base exponent =
  match exponent with 0 -> 1 | n -> base * power base (n - 1)

let count_overlap line =
  let extract_scratch_card_data line =
    let parse_numbers_to_array str =
      String.trim str |> String.split_on_char ' '
      |> List.filter (fun c -> not (String.equal c String.empty))
      |> List.map (fun d -> int_of_string d)
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
  List.length overlap

let process_line_part1 line =
  let ovelap_count = count_overlap line in
  match ovelap_count with 0 -> 0 | n -> power 2 (n - 1)

let print_array arr =
  Array.iter
    (fun d ->
      print_int d;
      print_string ", ")
    arr

(* 4 2 2 1 0 0*)

let process_part2 =
  let lines = read_lines "day4.txt" in
  let overlaps = Array.of_list (List.map count_overlap lines) in
  let card_counts = Array.init (Array.length overlaps) (fun _ -> 1) in

  let rec increment_subsequent_counts index iter count =
    match iter with
    | 0 -> ()
    | _ ->
        Array.set card_counts index (Array.get card_counts index + count);
        increment_subsequent_counts (index + 1) (iter - 1) count
  in

  let calculate_winnings game_index overlap_count =
    let card_count = Array.get card_counts game_index in
    increment_subsequent_counts (game_index + 1) overlap_count card_count;

    card_count
  in

  let winnings = Array.mapi calculate_winnings overlaps in
  print_array winnings;

  let rec get_last_element = function
    | [] -> failwith "No elements"
    | [ x ] -> x
    | h :: tl -> get_last_element tl
  in

  let last_element = get_last_element (Array.to_list winnings) in
  let sum = Array.fold_left ( + ) 0 winnings in

  sum - last_element

let process_part1 =
  let lines = read_lines "day4.txt" in
  let wins = List.map process_line_part1 lines in
  List.fold_left ( + ) 0 wins

let () = process_part2 |> print_int
