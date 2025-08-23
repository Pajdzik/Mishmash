let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'
  |> List.filter (fun x -> x <> "")

let print_int_list arr =
  List.iter (fun x -> print_string (string_of_int x ^ ", ")) arr;
  print_newline ()

let standarize_input lines =
  match lines with
  | [ line ] ->
      let number_chars = String.to_seq line |> List.of_seq in
      let has_free_space_at_the_end = List.length number_chars mod 2 == 0 in
      let numbers_without_free_space_chars =
        match has_free_space_at_the_end with
        | true ->
            List.filteri
              (fun i _ -> i < List.length number_chars - 1)
              number_chars
        | false -> number_chars
      in
      let numbers =
        List.map
          (fun c -> int_of_char c - int_of_char '0')
          numbers_without_free_space_chars
      in
      numbers
  | _ -> failwith "Invalid input"

type file = { id : int; size : int }

let split_numbers_into_groups numbers =
  let rec split_numbers_into_groups' file_id files spaces numbers =
    match numbers with
    | [] -> (files, spaces)
    | [ last_file_size ] ->
        ({ id = file_id; size = last_file_size } :: files, spaces)
    | file_size :: empty_size :: rest ->
        split_numbers_into_groups' (file_id + 1)
          ({ id = file_id; size = file_size } :: files)
          (empty_size :: spaces) rest
  in
  let files, spaces = split_numbers_into_groups' 0 [] [] numbers in
  (List.rev files, List.rev spaces)

let calculate_file_checksum file_id list_id file_size =
  let rec calculate_file_checksum' file_id list_id file_size check_sum =
    match file_size with
    | 0 -> (check_sum, list_id, file_size)
    | _ ->
        let check_sum' = check_sum + (list_id * file_id) in
        calculate_file_checksum' file_id (list_id + 1) (file_size - 1)
          check_sum'
  in

  calculate_file_checksum' file_id list_id file_size 0

let calculate_checksum files spaces =
  let rec calculate_checksum' checksum list_id files spaces =
    print_endline (Printf.sprintf "checksum: %d\tlist_id: %d" checksum list_id);
    match files with
    | [] -> checksum
    | file :: rest_files ->
        let file_checksum, list_id', _ =
          calculate_file_checksum file.id list_id file.size
        in

        let space, rest_spaces =
          match spaces with [] -> failwith "Invalid input" | s :: rs -> (s, rs)
        in

        let rev_files = List.rev files in
        let rev_file = List.hd rev_files in

        let moved_file_checksum, list_id'', remaining_file_size =
          calculate_file_checksum rev_file.id list_id' space
        in

        let whole_last_file_moved = space > rev_file.size in
        let files', spaces' =
          match whole_last_file_moved with
          | true ->
              let all_space_used = remaining_file_size == 0 in
              let rest_spaces' =
                match all_space_used with
                | true -> rest_spaces
                | false -> (space - rev_file.size) :: rest_spaces
              in

              ((List.rev (List.tl rev_files)), rest_spaces')
          | false -> (rest_files, rest_spaces)
        in

        let checksum' = checksum + file_checksum + moved_file_checksum in
        calculate_checksum' checksum' list_id'' files' spaces'
  in

  calculate_checksum' 0 0 files spaces

let process lines =
  let numbers = standarize_input lines in
  let files, spaces = split_numbers_into_groups numbers in
  calculate_checksum files spaces

let () =
  read_lines "day9.test.txt" |> process |> print_int;
  print_newline ()
