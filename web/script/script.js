/* 使用ライブラリ一覧

scrollreveal.js from https://scrollrevealjs.org
アニメーションライブラリ
*/


// アニメーションライブラリの初期化
window.sr = ScrollReveal();
sr.reveal('.rv');


// Buttons
// フロア切り替えボタンの要素を突っ込んだ配列
var btns = [
	document.getElementById("1f"),
	document.getElementById("2f"),
	document.getElementById("3f")
];

// Screens
// かくフロアのテーブルが並んだ画面のスクリーンの要素配列
var scns = [
	document.getElementById("1F_screen"),
	document.getElementById("2F_screen"),
	document.getElementById("3F_screen")
];


// Floor No
// フロア番号を表示する要素
var fno = document.getElementById("disp_flo");
 


// btnsの各ボタンに対してclickイベントのリスナーを追加
for ( var i = 0;  i < btns.length;  i++  ) {

	(function(elm, index) {
		elm.addEventListener("click", function () {

			// index = 0 (一階)だった場合1Fのスクリーンを表示可能にし0+1=(2階)と0+2(3階)は非表示にする
			if ( index == 0 ) {
				scns[index + 1].classList.add("hidden");
				scns[index + 2].classList.add("hidden");
	
				scns[index].classList.remove("hidden");
	
				fno.innerText = "F1";
			} 
			
			// index = 1 (2階)だった場合1Fのスクリーンを表示可能にし1-1=(1階)と1+1(3階)は非表示にする
			if ( index == 1 ) {
				scns[index - 1].classList.add("hidden");
				scns[index + 1].classList.add("hidden");
	
				scns[index].classList.remove("hidden");
	
				fno.innerText = "F2";
			} 
	
			// index = 2 (3階)だった場合1Fのスクリーンを表示可能にし2-1=(2階)と2-2(1階)は非表示にする
			if ( index == 2 ) {
				scns[index - 1].classList.add("hidden");
				scns[index - 2].classList.add("hidden");
	
				scns[index].classList.remove("hidden");
	
				fno.innerText = "F3";
			}
	
			// アニメーションの発行
			sr.reveal('.rv');
		});
	})(btns[i], i);
}
