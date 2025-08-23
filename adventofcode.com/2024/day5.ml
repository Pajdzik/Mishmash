let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'

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

let parse_update update_line = 
  let parts =  String.split_on_char ',' update_line in
  List.map (fun p -> int_of_string p) parts

let mid_element updates =
  List.nth updates (List.length updates / 2)

let process_part1 lines =
  let must_be_after_map, update_lines_raw = load_after_map lines in

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
    | true -> mid_element line
  in

  let update_lines = List.map parse_update update_lines_raw in
  let valid_updates = List.map (check_updates IntSet.empty) update_lines in
  let results = List.map2 count_results valid_updates update_lines in
  List.fold_left (fun acc el -> acc + el) 0 results

let process_part2 lines =
  let must_be_after_map, update_lines_raw = load_after_map lines in

  let process_updates updates_line = 
    let updates = parse_update updates_line in
    let visited = IntSet.empty in

    let rec topological_sort node stack =
     let all_numbers_that_have_to_be_after = Array.get must_be_after_map node in
     match all_numbers_that_have_to_be_after with 
     | [] -> stack
     |

      ()
    in

    let rec visit_each_node stack updates =
      match updates with
      | [] -> stack
      | node::rest -> 
        let was_already_visisted = IntSet.find_opt node visited in
        match was_already_visisted with
        | Some _ -> ();
        | None -> topological_sort node stack; 

        visit_each_node stack rest 
    in

    let stack = [] in
    let final_stack = visit_each_node stack updates in
    0


let () = read_lines "day5.txt" |> process_part2 |> print_int; print_newline()
