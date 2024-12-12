let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'
  |> List.filter (fun x -> x <> "")

let print_str_list arr =
  List.iter
    (fun x ->
      print_endline x;
      print_string ", ")
    arr;

  print_newline ()

let print_int_list arr =
  List.iter
    (fun x ->
      print_int x;
      print_string ", ")
    arr;

  print_newline ()

let process lines =
  let parse_line line =
    let parts = String.split_on_char ':' line in
    match parts with
    | [ result_str; rest_str ] ->
        let numbers_and_empty_strings = String.split_on_char ' ' rest_str in
        let numbers =
          List.filter (fun x -> String.trim x <> "") numbers_and_empty_strings
        in
        (int_of_string result_str, List.map int_of_string numbers)
    | _ -> failwith "Invalid input"
  in

  let rec process_line result numbers current_result =
    match result with
    | result when result == current_result && List.is_empty numbers -> result
    | result when result < current_result -> 0
    | result -> (
        match numbers with
        | [] -> 0
        | num :: rest ->
            let next_check = process_line result rest in
            let match_with_addition = next_check (current_result + num) in
            let match_with_multiplication = next_check (current_result * num) in
            if match_with_addition > 0 || match_with_multiplication > 0 then
              result
            else 0)
  in

  lines |> List.map parse_line
  |> List.map (fun (result, numbers) -> process_line result numbers 0)
  |> List.fold_left (fun acc x -> acc + x) 0

let () =
  read_lines "day7.txt" |> process |> print_int;
  print_newline ()
