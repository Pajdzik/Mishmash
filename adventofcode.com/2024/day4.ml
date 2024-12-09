let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'


let process_part1 lines =
  let arr = Array.of_list (List.map (fun s -> String.to_seq s |> Array.of_seq) lines) in
  let m = Array.length arr in
  let n = Array.length (Array.get arr 0) in
  let get_el = fun row col -> Array.get (Array.get arr row) col in

  let rec search_one_way = fun di dj i j searched_letter -> 
    match i, j with 
    | i, _ when i < 0 -> false
    | i, _ when i >= m -> false
    | _, j when j < 0 -> false
    | _, j when j >= n -> false
    | i, j -> 
      match (get_el i j) with
      | c when c <> searched_letter -> false
      | c -> 
        let new_i = i + di in
        let new_j = j + dj in
        let next_step = search_one_way di dj new_i new_j in

        match searched_letter with
        | 'X' -> next_step 'M'
        | 'M' -> next_step 'A'
        | 'A' -> next_step 'S'
        | 'S' -> true
        | _ -> false
  in

  let find_xmas = fun i j -> 
    (* This starts searching from index i j *)
    [(-1, -1); (-1, 0); (-1, 1); (0, -1); (0, 1); (1, -1); (1, 0); (1, 1)] |>
    List.map (fun (di, dj) -> search_one_way di dj i j 'X') |>
    List.map (fun el -> 
      match el with
      | true -> 1
      | false -> 0
    ) |>
    List.fold_left (fun acc el -> acc + el) 0
  in

  let mapped_arr = Array.mapi (fun i row -> Array.mapi (fun j _ -> find_xmas i j) row) arr in
  let sum_row row = Array.fold_left (fun acc el -> acc + el) 0 row in
  let summed_rows = Array.map sum_row mapped_arr in
  let result = Array.fold_left (fun acc el -> acc + el) 0 summed_rows in
  result

let () = read_lines "day4.txt" |> process_part1 |> print_int
