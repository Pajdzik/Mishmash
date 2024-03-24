module IntMap = Map.Make (Int)
module StringMap = Map.Make (String)

let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char ','

let rec hash_value value index sequence =
  match index with
  | i when String.length sequence <= i -> value
  | i ->
      let c = String.get sequence i in
      let ascii_code = Char.code c in
      let new_value = (value + ascii_code) * 17 mod 256 in
      hash_value new_value (index + 1) sequence

let process_part1 sequences =
  sequences |> List.map (hash_value 0 0) |> List.fold_left ( + ) 0

let print_string_list list =
  List.iter (fun s -> print_string s) list;
  print_newline ()

let print_int_list list =
  List.iter
    (fun s ->
      print_int s;
      print_string ", ")
    list;
  print_newline ()

let process_part2 sequences =
  let process_addition sequence label_to_focal_length_map =
    let parts = String.split_on_char '=' sequence in
    match parts with
    | [ label; focal_length_str ] ->
        let focal_length = int_of_string focal_length_str in
        let add_to_list = function
          | None -> Some focal_length
          | Some l -> Some focal_length
        in

        StringMap.update label add_to_list label_to_focal_length_map
    | _ -> failwith "Unrecognized addition format"
  in

  let process_removal sequence label_to_focal_length_map =
    let parts = String.split_on_char '-' sequence in
    match parts with
    | [ label; _ ] -> StringMap.remove label label_to_focal_length_map
    | _ -> failwith "Unrecognized removal format"
  in

  let process_sequence sequence label_to_focal_length_map =
    let process_fun =
      match sequence with
      | s when String.contains s '-' -> process_removal
      | s when String.contains s '=' -> process_addition
      | _ -> failwith "Unrecognized input"
    in

    process_fun sequence label_to_focal_length_map
  in

  let rec build_map label_to_focal_length_map = function
    | [] -> label_to_focal_length_map
    | sequence :: rest ->
        let new_maps = process_sequence sequence label_to_focal_length_map in
        build_map new_maps rest
  in

  let print_map =
    StringMap.iter (fun k v ->
        print_string k;
        print_string " -> ";
        print_int_list v;
        print_newline ())
  in

  let empty_map = StringMap.empty in
  let label_to_focal_length_map = build_map empty_map sequences in
  let map = StringMap.empty in
  let f = StringMap.to_seq label_to_focal_length_map |> Seq.map (fun (k, v) -> (hash_value 0 0 k, v)) in
  

  (* print_map map; *)
  (* StringMap.to_seq map
  |> Seq.map (fun (key, focal_length) -> (hash_value 0 0 key, focal_length))
  |> Seq.map (fun (hash_value, focal_length) ->
         let focal_lengths_times_index =
           List.mapi (fun i v -> (i + 1) * v) focal_lengths
         in
         let focal_lengths_times_hash_value =
           List.map (fun v -> v * hash_value) focal_lengths_times_index
         in
         List.fold_left ( + ) 0 focal_lengths_times_hash_value)
  |> Seq.fold_left ( + ) 0 *)

let () = read_lines "day15.test.txt" |> process_part2 |> print_int
