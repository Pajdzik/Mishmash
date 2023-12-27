let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all 
  |> String.split_on_char '\n'

let rec print_int_list = function
  | [] -> ()
  | h::t -> print_int h ; print_char ',' ; print_int_list(t)

let reverse_list l = 
  let rec reverse_aux acc = function 
  | [] -> acc
  | h::t -> reverse_aux (h::acc) t in
  reverse_aux [] l 

let rec extract_numbers l : int =
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

let process_part1 (input_lines : string list) = 
  let rec process_aux = function
  | [] -> 0
  | h::t -> (process_single_line h) + (process_aux t) in
  process_aux input_lines

let tokenize line = 
  let rec tokenize_aux l = 
    match l with 
    | [] -> []
    | d::t when d >= '0' && d <= '9' -> (int_of_char d - int_of_char '0') :: tokenize_aux(t)
    | 'o'::'n'::'e'::t -> 1 :: tokenize_aux('e' :: t)
    | 't'::'w'::'o'::t -> 2 :: tokenize_aux('o' :: t)
    | 't'::'h'::'r'::'e'::'e'::t -> 3 :: tokenize_aux('e' :: t)
    | 'f'::'o'::'u'::'r'::t -> 4 :: tokenize_aux(t)
    | 'f'::'i'::'v'::'e'::t -> 5 :: tokenize_aux('e' :: t)
    | 's'::'i'::'x'::t -> 6 :: tokenize_aux(t)
    | 's'::'e'::'v'::'e'::'n'::t -> 7 :: tokenize_aux('n' :: t)
    | 'e'::'i'::'g'::'h'::'t'::t -> 8 ::tokenize_aux('t' :: t)
    | 'n'::'i'::'n'::'e'::t -> 9 :: tokenize_aux('e' :: t)
    | h::t -> tokenize_aux(t) in

    match line with
      | "" -> [0]
      | l -> tokenize_aux (List.of_seq (String.to_seq l))
  
let number_from_first_and_last_digits l =
    let first = List.hd l in
    let last = (List.hd (List.rev l)) in
    let res = 10 * first + last in
    print_int_list l;
    print_string " | ";
    print_int_list [first; last; res];
    print_endline "";
    res

let extract_number line =
  let tokens = tokenize line in
  number_from_first_and_last_digits tokens

let process_part2 (input_lines : string list) = 
  let extracted_numbers = List.map extract_number input_lines in
  List.fold_left ( + ) 0 extracted_numbers

let test =
  assert (extract_number "two1nine" = 29);
  assert (extract_number "eightwothree" = 83);
  assert (extract_number "abcone2threexyz" = 13);
  assert (extract_number "xtwone3four" = 24);
  assert (extract_number "xtwone3fiveeight" = 28);
  assert (extract_number "eightfivetwone" = 81)

let () = 
  test;
  let input_lines = read_lines "day1.txt" in
  process_part2 input_lines |> string_of_int |> print_endline