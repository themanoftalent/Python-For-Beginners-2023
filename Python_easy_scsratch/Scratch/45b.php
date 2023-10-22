<?php

$python = exec('python C:/Users/Raunak/Desktop/tutorials/45a.py');

$data = file_get_contents('name.json');
$display_data = json_decode($data, true);
foreach ($display_data as $dd) {
	echo $dd."<br>";
}




//echo $python;




?>