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
            prize = (fst p + 10000000000000, snd p + 10000000000000);
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

(*
  Minimize the cost of reaching the prize by using the buttons A and B.
  The prize is at the coordinates (Px, Py).
  The buttons A and B move the player by the vectors (Ax, Ay) and (Bx, By) respectively.
  Ca = 3, Cb = 1

  Minimize:
  C = 3 * [Na] + 1 * [Nb]

  Px = [Na] * Ax + [Nb] * Bx
  Py = [Na] * Ay + [Nb] * By

  [Na] = (By * Px - Bx * Py) / (Ax * By - Ay * Bx)
  [Nb] = (-Ay * Px + Ax * Py) / (Ax * By - Ay * Bx)
*)

let count_moves (input : input) =
  let px, py = input.prize in
  let ax, ay = input.button_a.vec in
  let bx, by = input.button_b.vec in
  let denominator = ax * by - ay * bx in
  let button_a_count = (by * px - bx * py) / denominator in
  let button_b_count = (ax * py - ay * px) / denominator in

  let can_reach =
    button_a_count >= 0 && button_b_count >= 0
    && (button_a_count * ax + button_b_count * bx = px)
    && (button_a_count * ay + button_b_count * by = py) in

  match can_reach with
  | false -> 0
  | true -> button_a_count * 3 + button_b_count

let process lines =
  lines |> parse_input |> List.map count_moves |> List.fold_left ( + ) 0

let () =
  read_lines "day13.txt" |> process |> print_int;
  print_newline ()
 