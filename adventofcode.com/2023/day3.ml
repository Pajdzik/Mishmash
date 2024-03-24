let read_array file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'
  |> List.map (fun line -> String.to_seq line |> Array.of_seq)
  |> Array.of_list

let print_char_list arr = Array.iter (fun arr -> Array.iter print_char arr) arr

type char_type = Digit | Char | Dot

let char_type = function '0' .. '9' -> Digit | '.' -> Dot | _ -> Char

let process_part1 (input : char array array) =
  let look_for_adjacent_number (arr : char array array) row_index column_index =
    let c = Array.get (Array.get arr row_index) column_index in
    ()
  in

  let process_cell (arr : char array array) row_index column_index cell =
    match char_type cell with
    | Dot -> ()
    | Digit -> ()
    | Char -> look_for_adjacent_number arr row_index column_index
  in

  let process_rows row_index row =
    Array.iteri (process_cell input row_index) row
  in

  Array.iteri process_rows input

let () =
  let input = read_array "day3.txt" in
  print_char_list input
