let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'
  |> List.filter (fun x -> x <> "")

type vec = int * int
type button = { cost : int; vec : vec }
type input = { button_a : button; button_b : button; prize : vec }

let print_str_list lst =
  List.iter (fun x -> print_string (x ^ ", ")) lst;
  print_newline ()

let print_input_list arr =
  List.iter
    (fun x ->
      Printf.printf "A: (%d %d), B: (%d %d), P: (%d %d)" (fst x.button_a.vec)
        (snd x.button_a.vec) (fst x.button_b.vec) (snd x.button_b.vec)
        (fst x.prize) (snd x.prize))
    arr;
  print_newline ()

let parse_input (lines : string list) =
  let parse_numbers line =
    let parse_number s =
      String.to_seq s
      |> Seq.filter (fun c -> Char.code c >= 48 && Char.code c <= 57)
      |> String.of_seq |> int_of_string
    in

    let parts = String.split_on_char ' ' line in
    match parts with
    | [ _; x_str; y_str ] | [ _; _; x_str; y_str ] ->
        let x = parse_number x_str in
        let y = parse_number y_str in
        (x, y)
    | _ -> failwith "More parts than expected"
  in

  let rec parse_input' acc lines =
    match lines with
    | [] -> acc
    | a :: b :: p :: rest ->
        let a = parse_numbers a in
        let b = parse_numbers b in
        let p = parse_numbers p in
        parse_input'
          ({
             button_a = { vec = a; cost = 3 };
             button_b = { vec = b; cost = 1 };
             prize = p;
           }
          :: acc)
          rest
    | _ -> failwith "Invalid input"
  in

  List.rev (parse_input' [] lines)

let vector_length vec =
  let x, y = vec in
  int_of_float (sqrt (float_of_int ((x * x) + (y * y))))

let vec_sub (x1, y1) (x2, y2) = (x1 - x2, y1 - y2)

(* A button cost: 3 *)
(* B button cost: 1 *)

let count_moves (input : input) =
  let b_length = vector_length input.button_b.vec in
  let a_length = vector_length input.button_a.vec in

  let more_optimal_move, less_optimal_move =
    if b_length * 3 < a_length then (input.button_a, input.button_b)
    else (input.button_b, input.button_a)
  in

  let vertical_full_moves = snd input.prize / snd more_optimal_move.vec in
  let horizontal_full_moves = fst input.prize / fst more_optimal_move.vec in
  let min_optimal_full_moves = min vertical_full_moves horizontal_full_moves in

  let backwards_starting_point =
    ( min_optimal_full_moves * fst more_optimal_move.vec,
      min_optimal_full_moves * snd more_optimal_move.vec )
  in

  let rec fill_the_rest_with_less_optimal_moves optimal_moves_count
      (starting_point : vec) =
    print_endline
      (Printf.sprintf "start: %d %d" (fst starting_point) (snd starting_point));
    let x, y = starting_point in
    if x < 0 || y < 0 then (0, 0)
    else
      let prize_x, prize_y = input.prize in
      let diff_x = prize_x - x in

      let mod_x = diff_x mod fst less_optimal_move.vec in
      let move_count = diff_x / fst less_optimal_move.vec in
      let y_after_move = y + (move_count * snd less_optimal_move.vec) in
      let can_be_reached = y_after_move = prize_y in
      if mod_x = 0 && can_be_reached then (optimal_moves_count, move_count)
      else
        fill_the_rest_with_less_optimal_moves (optimal_moves_count - 1)
          (vec_sub starting_point more_optimal_move.vec)
  in

  let optimal_moves_count, less_optimal_moves_count =
    fill_the_rest_with_less_optimal_moves min_optimal_full_moves
      backwards_starting_point
  in

  print_endline
    (Printf.sprintf "optimal: %d, less optimal: %d" optimal_moves_count
       less_optimal_moves_count);
  print_endline
    (Printf.sprintf "more optimal: %d, less optimal: %d" more_optimal_move.cost
       less_optimal_move.cost);

  let result =
    (optimal_moves_count * more_optimal_move.cost)
    + (less_optimal_moves_count * less_optimal_move.cost)
  in

  print_endline (Printf.sprintf "result: %d" result);

  result

let process lines =
  lines |> parse_input |> List.map count_moves |> List.fold_left ( + ) 0

let () =
  read_lines "day13.txt" |> process |> print_int;
  print_newline ()
