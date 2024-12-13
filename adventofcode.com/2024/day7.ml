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

  let common_suffix res el =
    let rec common_suffix_aux res el shift =
      match el with
      | 0 -> (true, shift)
      | e -> (
          let res_last_digit = res mod 10 in
          let e_last_digit = e mod 10 in
          match res_last_digit = e_last_digit with
          | false -> (false, shift)
          | true -> common_suffix_aux (res / 10) (e / 10) (shift + 1))
    in
    common_suffix_aux res el 0
  in

  let pow_10 n =
    let rec pow_10_aux n acc =
      match n with 0 -> acc | n -> pow_10_aux (n - 1) (acc * 10)
    in
    pow_10_aux n 1
  in

  let rec process_line numbers result =
    match result with
    | 0 -> List.is_empty numbers
    | result -> (
        match numbers with
        | [] -> false
        | _ ->
            let el = List.hd numbers in
            let is_divisible = result mod el = 0 in
            let with_multiplication =
              if is_divisible then process_line (List.tl numbers) (result / el)
              else false
            in

            let has_common_suffix, length = common_suffix result el in
            let with_common_suffix =
              if has_common_suffix then
                process_line (List.tl numbers) (result / pow_10 length)
              else false
            in

            let with_addition = process_line (List.tl numbers) (result - el) in

            with_multiplication || with_common_suffix || with_addition)
  in

  let parsed_lines = lines |> List.map parse_line in
  let can_be_achieved =
    List.map
      (fun (result, numbers) -> process_line (List.rev numbers) result)
      parsed_lines
  in

  List.fold_left2
    (fun acc line flag -> if flag then acc + fst line else acc)
    0 parsed_lines can_be_achieved

let () =
  read_lines "day7.txt" |> process |> print_int;
  print_newline ()
