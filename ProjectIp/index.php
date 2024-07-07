<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Floating Input Box on Map</title>
    <style>
    body {
        margin: 0;
        font-family: Arial, sans-serif;
        background-color: black;
    }
    #map-container {
        position: relative;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        background-color: black;
    }
    #floating-input {
        position: absolute;
        top: 20px; /* Adjust as needed */
        left: 50%; /* Center horizontally */
        transform: translateX(-50%);
        z-index: 1000;
        background-color: rgba(255, 255, 255, 0.2);
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        color: white;
        border: white;
    }

    #input-box{        
        color: white;
        border: solid white;
        background-color: rgba(255, 255, 255, 0.1);
    }
    #input-box::-webkit-input-placeholder {
        color: white;
    }

    /* #map_c0d489226447f29158dc96929f44cb0e {
        background-color: black;
    } */

</style>
</head>
<body>
    <div id="map-container">

<?php


 $html_file = 'world_map.html';
 if (file_exists($html_file)) {
     echo file_get_contents($html_file);
 } else {
     echo "<p>Map not found.</p>";
 }

 
?>
<div id="floating-input">
            <input type="text" placeholder="Enter the IP address" id="input-box">
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            $('#input-box').on('keypress', function(e) {
                if (e.which == 13) { // Enter key pressed
                    var ipAddress = $(this).val();
                    $.ajax({
                        url: 'process.php',
                        type: 'POST',
                        data: { input: ipAddress },
                        success: function(response) {
                            console.log('Python script output:', response, ipAddress);
                            alert('Python script executed successfully.');                            
                            location.reload();
                        },
                        error: function(error) {
                            console.error('Error:', error);
                            alert('An error occurred.');
                        }
                    });
                }
            });
        });
    </script>

</body>
</html>