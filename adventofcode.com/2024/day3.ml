#load "str.cma"
open Str

let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'

let rec find_and_multiply acc start_index should_skip lines = 
  match lines with
  | [] -> acc
  | line::rest ->
    try 
      let re = Str.regexp {|mul(\([0-9]+\),\([0-9]+\))\|don't()\|do()|} in
      let found_index = Str.search_forward re line start_index in
      let matched_fragment = Str.matched_group 0 line in
      let next_index = found_index + String.length matched_fragment in

      print_endline ("Matched: " ^ matched_fragment ^ "\tskip:" ^ (string_of_bool should_skip));

      match matched_fragment with
      | s when String.starts_with ~prefix:"don't" s -> find_and_multiply acc next_index true lines 
      | s when String.starts_with ~prefix:"do" s -> find_and_multiply acc next_index false lines 
      | s ->
        let add = match should_skip with
        | true -> 0
        | false -> 
          let first = int_of_string (Str.matched_group 1 line) in
          let second = int_of_string (Str.matched_group 2 line) in
          (first * second) in
        
        find_and_multiply (acc + add) next_index should_skip lines
    with Not_found -> find_and_multiply acc 0 should_skip rest
  
let process_line lines =
  (find_and_multiply 0 0 false lines)

let process_part2 lines =
  lines |>
  process_line

let () = read_lines "day3.txt" |> process_part2 |> print_int; print_newline()
