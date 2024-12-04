#load "str.cma"
open Str


let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'

let rec find_and_multiply acc start_index line = 
  try 
    let found_index = Str.search_forward (Str.regexp "mul(\\([0-9]+\\),\\([0-9]+\\))") line start_index in
    let first = int_of_string (Str.matched_group 1 line) in
    let second = int_of_string (Str.matched_group 2 line) in
    let next_index = found_index + String.length (Str.matched_group 0 line) in
    
    find_and_multiply (acc + first * second) next_index line
  with Not_found -> acc
  
let process_line line =
  let res = (find_and_multiply 0 0 line) in
  res

let process_part1 lines =
  lines |>
  List.map process_line |>
  List.fold_left (fun acc el -> acc + el) 0 

let () = read_lines "day3.txt" |> process_part1 |> print_int
