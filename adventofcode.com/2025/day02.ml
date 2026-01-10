let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char ','
  |> List.filter (fun x -> x <> "")

let parse_range line =
  let parts = String.split_on_char '-' (String.trim line) in
  match parts with
  | [start_str; end_str] ->
      let start_num = int_of_string start_str in
      let end_num = int_of_string end_str in
      (start_num, end_num)
  | _ -> failwith "Invalid range format"

let rec int_pow base exp =
  match exp with
  | 0 -> 1
  | 1 -> base
  | _ -> base * int_pow base (exp - 1)

let num_len num = 
  String.length (string_of_int num)

let first_half_of_a_number num =
  let number_len = num_len num in
  let half_length = number_len / 2 in
  let divisor = int_pow 10 half_length in
  num / divisor

let find_next_even_length num =
  let number_len = num_len num in
  if number_len mod 2 = 0 then
    num
  else
    int_pow 10 (number_len)

let concat_numbers num1 num2 =
  let str1 = string_of_int num1 in
  let str2 = string_of_int num2 in
  int_of_string (str1 ^ str2)

let repeated_first_half num =
  let first_half = first_half_of_a_number num in
  concat_numbers first_half first_half

let process_part1 ranges =
  let is_number_in_range num range =
    let start = fst range in
    let end_ = snd range in
    num >= start && num <= end_
  in

  let process_range range = 
    let start = fst range in
    let end_ = snd range in
    let even_start = find_next_even_length start in
    let double_half_start = repeated_first_half even_start in
    Printf.sprintf "Processing range: %d - %d | Starting at: %d" start end_ double_half_start |> print_endline;

    let rec process_range_aux current count = 
      if current > end_ then count
      else
        let first_half = first_half_of_a_number current in
        Printf.sprintf "Checking number: %d | First half: %d" current first_half |> print_endline;
        let repeated = concat_numbers first_half first_half in
        let is_in_range = is_number_in_range repeated range in
        let new_count = if is_in_range  then
           (count + current)
          else 
            count 
          in

        if is_in_range then
          print_endline (Printf.sprintf "  Included: %d" repeated)
        else
          ();

        let next_number = concat_numbers (first_half + 1) (first_half + 1) in
        Printf.sprintf "  Next number to check: %d" next_number |> print_endline;
        process_range_aux next_number new_count
      in

    process_range_aux double_half_start 0
  in

  ranges |> List.map process_range |> List.fold_left (+) 0


let process lines =
  let ranges = List.map parse_range lines in
  process_part1 ranges


let () =
  read_lines "day02.txt" |> process |> print_int;
  print_newline ()
