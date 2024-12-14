let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'
  |> List.filter (fun x -> x <> "")
  |> List.map (fun l -> l |> String.to_seq |> List.of_seq)

module IntTuple = struct
  type t = int * int

  let compare (a1, b1) (a2, b2) =
    match Int.compare a1 a2 with 0 -> Int.compare b1 b2 | n -> n
end

module CharMap = Map.Make (Char)
module TupleSet = Set.Make (IntTuple)

let print_char_map map =
  CharMap.iter
    (fun k v ->
      Printf.printf "%c: " k;
      List.iter (fun (a, b) -> Printf.printf "(%d, %d) " a b) v;
      print_newline ())
    map

let print_tuple_set set =
  TupleSet.iter (fun (a, b) -> Printf.printf "(%d, %d) " a b) set

let process_part1 lines =
  let m = List.length lines in
  let n = List.length (List.hd lines) in
  let rec find_antenna_positions map (lines : char list list) =
    let rec find_antenna_positions_in_a_line map (row, col) line =
      match line with
      | [] -> map
      | c :: rest ->
          let new_map =
            match c with
            | '.' -> map
            | _ ->
                CharMap.update c
                  (fun v ->
                    match v with
                    | None -> Some [ (row, col) ]
                    | Some arr -> Some ((row, col) :: arr))
                  map
          in

          find_antenna_positions_in_a_line new_map (row, col + 1) rest
    in

    let rec find_antenna_positions' map row lines =
      match lines with
      | [] -> map
      | line :: rest ->
          let new_map = find_antenna_positions_in_a_line map (row, 0) line in
          find_antenna_positions' new_map (row + 1) rest
    in
    find_antenna_positions' map 0 lines
  in

  let process_antenna_type set (positions : (int * int) list) =
    let cartesian_product lst =
      List.concat (List.map (fun x -> List.map (fun y -> (x, y)) lst) lst)
    in
    let position_pairs = cartesian_product positions in
    let rec process_position_pairs set position_pairs =
      match position_pairs with
      | [] -> set
      | ((x, y), (x', y')) :: rest -> (
          match (x = x', y = y') with
          | true, true -> process_position_pairs set rest
          | _, _ ->
            let add_if_valid (x, y) set  =
              match (x >= 0 && x < m, y >= 0 && y < n) with
              | true, true -> TupleSet.add (x, y) set
              | _, _ -> set
            in

            let diff_x = x' - x in
            let diff_y = y' - y in
            let first_antinode = (x - diff_x, y - diff_y) in
            let second_antinode = (x' + diff_x, y' + diff_y) in
            let new_set = add_if_valid first_antinode set in
            let new_set' = add_if_valid second_antinode new_set in
            process_position_pairs new_set' rest)
    in
    process_position_pairs set position_pairs
  in

  let antenna_positions = find_antenna_positions CharMap.empty lines in
  let values = CharMap.to_list antenna_positions |> List.map (fun (k, v) -> v) |> List.map (process_antenna_type TupleSet.empty) in
  let set = List.fold_left (fun ss s -> TupleSet.union ss s) TupleSet.empty values in
  print_tuple_set set;
  print_newline ();
  TupleSet.cardinal set

let () =
  read_lines "day8.txt" |> process_part1 |> print_int;
  print_newline ()
