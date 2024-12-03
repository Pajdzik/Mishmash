let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'

let print_int_list arr =
  List.iter
    (fun x ->
      print_int x;
      print_string ", ")
    arr;

  print_newline ()

let parse_lines lines = 
    let split_line line = String.split_on_char ' ' line in
    let parse_line line = List.map (fun x -> (int_of_string x)) (split_line line) in
     List.map parse_line lines

let find_sign arr = match arr with
  | x::y::rest -> if x - y >= 0 then -1 else 1
  | _ -> failwith "Invalid input"

let rec is_safe_sign allow_error arr sign = 
  print_int_list arr;  
  
  match arr with
  | [] -> true
  | [_] -> true
  | x::y::rest ->
    let d = sign*(y - x) in
    match d with
    | _ when d >= 1 && d<=3 -> is_safe_sign allow_error (y::rest) sign
    | _ when allow_error -> is_safe_sign false (y::rest) sign
    | _ -> false

let is_safe allow_error arr  = 
  let sign = find_sign arr in
  is_safe_sign allow_error arr sign

let process_part1 lines =
    let safe_lines = List.map (is_safe false) lines in
    List.fold_left (fun acc b -> if b then acc + 1 else acc) 0 safe_lines

let process_part2 lines =
  let safe_lines = List.map (is_safe true) lines in
  List.fold_left (fun acc b -> if b then acc + 1 else acc) 0 safe_lines

let () = read_lines "day2.txt" |> parse_lines |> process_part2 |> print_int
