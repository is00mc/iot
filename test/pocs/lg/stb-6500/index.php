<!DOCTYPE html>
<?php
    $dev = "192.168.25.180";
    if (isset($_POST['menu']))
    {
	    exec("python3 LG_test.py -dev $dev -mn");
    }
    elseif (isset($_POST['ok']))
    {
	    exec("python3 LG_test.py -dev $dev -ok");
    }
    elseif (isset($_POST['up']))
    {
	    exec("python3 LG_test.py -dev $dev -u");
    }
    elseif (isset($_POST['down']))
    {
	    exec("python3 LG_test.py -dev $dev -d");
    }
    elseif (isset($_POST['left']))
    {
	    exec("python3 LG_test.py -dev $dev -l");
    }
    elseif (isset($_POST['right']))
    {
	    exec("python3 LG_test.py -dev $dev -r");
    }
    elseif (isset($_POST['0']))
    {
	    exec("python3 LG_test.py -dev $dev -num 0");
    }
    elseif (isset($_POST['1']))
    {
	    exec("python3 LG_test.py -dev $dev -num 1");
    }
    elseif (isset($_POST['2']))
    {
	    exec("python3 LG_test.py -dev $dev -num 2");
    }
    elseif (isset($_POST['3']))
    {
	    exec("python3 LG_test.py -dev $dev -num 3");
    }
    elseif (isset($_POST['4']))
    {
	    exec("python3 LG_test.py -dev $dev -num 4");
    }
    elseif (isset($_POST['5']))
    {
	    exec("python3 LG_test.py -dev $dev -num 5");
    }
    elseif (isset($_POST['6']))
    {
	    exec("python3 LG_test.py -dev $dev -num 6");
    }
    elseif (isset($_POST['7']))
    {
	    exec("python3 LG_test.py -dev $dev -num 7");
    }
    elseif (isset($_POST['8']))
    {
	    exec("python3 LG_test.py -dev $dev -num 8");
    }
    elseif (isset($_POST['9']))
    {
	    exec("python3 LG_test.py -dev $dev -num 9");
    }
?>
<html>
<body>
    <form method="post">
    <p>
        <button align="center" name="menu">menu</button>
        <button name="ok">ok</button>
    </p>
    <p>
	<button name="up">up</button>
	<button name="down">down</button>
	<button name="left">left</button>
	<button name="right">right</button>
    </p>
    <p>
	<button name="1">1</button>
	<button name="2">2</button>
	<button name="3">3</button>
    </p>
    <p>
	<button name="4">4</button>
	<button name="5">5</button>
	<button name="6">6</button>
    </p>
    <p>
	<button name="7">7</button>
	<button name="8">8</button>
	<button name="9">9</button>
    </p>
    <p>
        <button name="0">0</button>
    </p>
    </form>
</body>
</html>
