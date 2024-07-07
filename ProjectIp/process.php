<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $input = $_POST['input'];
    // $escaped_input = escapeshellarg($input);
    echo $input;
    $command = 'python main.py ' . $input;
    $output = shell_exec($command);
    echo $output;
}
?>
