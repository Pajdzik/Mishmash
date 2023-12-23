let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all 
  |> String.split_on_char '\n'

let rec extract_numbers l : int =
  let reverse_list l = 
    let rec reverse_aux acc = function 
    | [] -> acc
    | h::t -> reverse_aux (h::acc) t in
    reverse_aux [] l in

  let is_digit = function
    | '0'..'9' -> true
    | _ -> false in

  let rec first_digit = function
    | h::t when (is_digit h) -> String.make 1 h
    | h::t -> first_digit t
    | [] -> "" in

  int_of_string ((first_digit l) ^ (first_digit (reverse_list l)))

let process_single_line line: int =
  match line with
  | "" -> 0
  | s -> extract_numbers (List.of_seq (String.to_seq s))

let process (input_lines : string list) = 
  let rec process_aux = function
  | [] -> 0
  | h::t -> (process_single_line h) + (process_aux t) in
  process_aux input_lines


let () = 
  let input_lines = read_lines "day1.txt" in
  process input_lines |> string_of_int |> print_endline

