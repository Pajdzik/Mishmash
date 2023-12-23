let process_lines filename (f: string -> unit) = 
  let input_channel = open_in filename in

  let rec read_line() = 
    let line = try input_line input_channel with End_of_file -> exit 0 in
    f line;
    read_line ()
  in read_line()

let rec extract_numbers l : string =
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

  let concatenated_digit_chars = (first_digit l) ^ (first_digit (reverse_list l))

let process line = 
  let line_list = List.of_seq (String.to_seq line) in
  extract_numbers line_list
  
let process_and_print line = 
  let result = process line in
  print_endline result

let () = 
  (* print_endline (extract_numbers (List.of_seq (String.to_seq "12asd3sa"))) *)
  let filename = "day1.txt" in
  process_lines filename process_and_print
