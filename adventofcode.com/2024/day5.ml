let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'

let print_string_list arr =
  List.iter
    (fun x ->
      print_string x;
      print_string ", ")
    arr;

  print_newline ()

module IntSet = Set.Make(Int)

let load_after_map lines = 
  let must_be_after_map = Array.init 100 (fun _ -> IntSet.empty) in

  let rec load_line lines = 
    match List.hd lines with
    | "" -> (must_be_after_map, List.tl lines)
    | s -> 
      let parts = String.split_on_char '|' s in
      let before, after = match parts with 
      | [before_str; after_str] -> int_of_string before_str, int_of_string after_str
      | _ -> failwith "Invalid input" in

      let set = Array.get must_be_after_map before in
      let updated_set = IntSet.add after set in
      Array.set must_be_after_map before updated_set;
      load_line (List.tl lines) in

  load_line lines

let process_input lines =
  let must_be_after_map, update_lines_raw = load_after_map lines in

  let parse_update (update_line: string) = 
    let parts =  String.split_on_char ',' update_line in
    List.map (fun p -> int_of_string p) parts
  in

  let rec check_updates seen updates =
    let update = List.hd updates in
    let all_numbers_that_have_to_be_after = Array.get must_be_after_map update in
    let intersection = IntSet.inter all_numbers_that_have_to_be_after seen in

    match IntSet.is_empty intersection with
    | false -> false
    | true ->
      let rest_of_the_updates = List.tl updates in
      match rest_of_the_updates with 
      | [] -> true
      | r -> 
        let new_seen = IntSet.add update seen in
        check_updates new_seen rest_of_the_updates
    in

  let count_results valid line = 
    match valid with
    | false -> 0
    | true -> List.nth line (List.length line / 2)
  in

  let update_lines = List.map parse_update update_lines_raw in
  let valid_updates = List.map (check_updates IntSet.empty) update_lines in
  let results = List.map2 count_results valid_updates update_lines in
  List.fold_left (fun acc el -> acc + el) 0 results

let process_part1 lines =
  lines |>
  process_input 
  (* List.map process_line |>
  List.fold_left (fun acc el -> acc + el) 0  *)

let () = read_lines "day5.txt" |> process_part1 |> print_int; print_newline()
