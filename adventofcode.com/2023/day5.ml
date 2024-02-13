type map_range = {
  destination_range_start : int;
  source_range_start : int;
  length : int;
}

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

let print_map_range mr =
  Printf.printf "[s: %d, d: %d, l: %d], " mr.source_range_start
    mr.destination_range_start mr.length

let print_map_range_list arr =
  List.iter print_map_range arr;

  print_newline ()

let rec list_min min = function
  | [] -> min
  | l ->
      let h = List.hd l in
      let next_min = match h with el when el < min -> el | _ -> min in
      list_min next_min (List.tl l)

let process_part1 lines =
  let seeds_line, rest_of_the_lines =
    match lines with
    | hd :: rest -> (hd, rest)
    | _ -> failwith "Unrecognized input"
  in

  (* seeds: 79 14 55 13 *)
  let seeds =
    let parts = String.split_on_char ':' seeds_line in
    let _, numbers_str =
      match parts with
      | [ label; numbers ] -> (label, String.trim numbers)
      | _ -> failwith "Unrecognized seeds format"
    in

    String.split_on_char ' ' numbers_str |> List.map int_of_string
  in

  let get_maps lines =
    let parse_range line =
      (* 45 77 23 *)
      let numbers = String.split_on_char ' ' line |> List.map int_of_string in

      match numbers with
      | [ d; s; l ] ->
          { destination_range_start = d; source_range_start = s; length = l }
      | _ -> failwith "Unrecognized range data"
    in

    let is_number_row s = String.length s > 0 && s.[0] >= '0' && s.[0] <= '9' in

    let rec parse_number_lines lines ranges =
      let line = match lines with [] -> "" | _ -> List.hd lines in

      match line with
      | s when is_number_row s ->
          let range = parse_range line in
          parse_number_lines (List.tl lines) (ranges @ [ range ])
      | _ ->
          List.sort
            (fun x y -> x.source_range_start - y.source_range_start)
            ranges
    in

    let rec drop_elements lines = function
      | 0 -> lines
      | n -> drop_elements (List.tl lines) (n - 1)
    in

    let rec parse_maps lines maps =
      match lines with
      | [] -> maps
      | ls -> (
          let head = List.hd ls in
          match head with
          | s when is_number_row s ->
              let ranges = parse_number_lines lines [] in
              let next_maps = maps @ [ ranges ] in
              let next_lines = drop_elements lines (List.length ranges) in
              parse_maps next_lines next_maps
          | _ -> parse_maps (List.tl lines) maps)
    in

    parse_maps (List.tl lines) []
  in

  let rec map_values maps value =
    let rec find_range value ranges =
      match ranges with
      | [] -> None
      | ranges -> (
          let range = List.hd ranges in
          let upper_limit = range.source_range_start + range.length in

          let falls_into_source_range =
            value >= range.source_range_start && value < upper_limit
          in
          match falls_into_source_range with
          | true -> Some range
          | _ -> find_range value (List.tl ranges))
    in

    match maps with
    | [] -> value
    | _ -> (
        let ranges = List.hd maps in
        let range = find_range value ranges in
        match range with
        | None -> map_values (List.tl maps) value
        | Some r ->
            let next_value =
              r.destination_range_start + (value - r.source_range_start)
            in
            map_values (List.tl maps) next_value)
  in

  let maps = get_maps lines in

  let mapped_seed_values = List.map (map_values maps) seeds in
  list_min Int.max_int mapped_seed_values

let () = read_lines "day5.txt" |> process_part1 |> print_int
