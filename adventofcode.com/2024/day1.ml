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

let foo parse_lines =
    let split_lines line  = match line with
        | "" -> failwith "Invalid input"
        | x -> match List.filter (fun s -> s <> "") (String.split_on_char ' ' x) with
            | [x;y] -> ((int_of_string x), (int_of_string y))
            | x -> failwith "Invalid input"
      in
    let parsed_lines = List.map split_lines parse_lines in

    let first_col, second_col = List.split parsed_lines in
    (first_col, second_col)

let process_part1 lines =
    let first_col, second_col = foo lines in
    let sorted_first_col = List.sort compare first_col in
    let sorted_second_col = List.sort compare second_col in
    let diffs = List.map2 (fun x y -> Int.abs(y - x)) sorted_first_col sorted_second_col in
    let sum = List.fold_left (+) 0 diffs in
    sum

let process_part2 lines =
    let first_col, second_col = foo lines in

    let score n = 
        let freq = List.fold_left (fun acc x -> if x = n then acc + 1 else acc) 0 second_col in
        freq * n
    in

    let scores = List.map score first_col in
    let sum = List.fold_left (+) 0 scores in
    sum

let () = read_lines "day1.txt" |> process_part2 |> print_int
