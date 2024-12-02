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

let print_string_list arr =
  List.iter
    (fun x ->
      print_string x;
      print_string ", ")
    arr;

  print_newline ()

let process_part1 lines =
    let parse_line line  = match line with
        | "" -> failwith "Invalid input"
        | x -> match List.filter (fun s -> s <> "") (String.split_on_char ' ' x) with
            | [x;y] -> ((int_of_string x), (int_of_string y))
            | x -> failwith "Invalid input"
      in
    let parsed_lines = List.map parse_line lines in

    let first_col, second_col = List.split parsed_lines in
    let sorted_first_col = List.sort compare first_col in
    let sorted_second_col = List.sort compare second_col in

    let diffs = List.map2 (fun x y -> Int.abs(y - x)) sorted_first_col sorted_second_col in
    let sum = List.fold_left (+) 0 diffs in
    sum

let () = read_lines "day1.txt" |> process_part1 |> print_int
