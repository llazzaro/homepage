/*-----------------------------------------------------------------------------------
 	My Custom JS for invictus Wordpress Theme
-----------------------------------------------------------------------------------*/
/*
	0. =Main Variable Settings
	1. =General Settings
	2. =Setup Supefish Pulldown menu
	3. =Setup Portfolio hover
	4. =Init Tipsy Tooltips 
	5. =Shortcode JS	
	6. =Contact Form Validation
	7. =Hide all elements
	8. =Hide Thumbnails

*/

// Init jQuery on page load
jQuery(document).ready(function($) {								

	if(navigator.platform == 'iPad' || navigator.platform == 'iPhone' || navigator.platform == 'iPod'){
		 $("#colophon").css("position", "static");
	};

/*-----------------------------------------------------------------------------------*/
/*	0. =Main Variable settings
/*-----------------------------------------------------------------------------------*/

	$brand     = $('#branding');
	$thumbs    = $('#thumbnails');
	$colophon  = $('#colophon');
	$togthumbs = $('#toggleThumbs');
	$expander  = $('#expander');
	$main	   = $('#main');
	$primary   = $('#primary');
	$scans	   = $('#scanlines');
	$sidebar   = $('#sidebar');
	$nav	   = $('nav#navigation');

/*-----------------------------------------------------------------------------------*/
/*	1. =General Settings
/*-----------------------------------------------------------------------------------*/

	// Custom delay functions
	$.fn.delay = function(time,func){

		return this.each(function(){
			setTimeout(func,time);
		});
		
	};
	
	// Slide Fade toggle
	$.fn.slideFadeToggle = function(speed, easing, callback) { 
		// nice slide fade toggle animation - pew pew pew
		return this.animate({opacity: 'toggle', height: 'toggle'}, speed, easing, callback);  
	}
	
/*-----------------------------------------------------------------------------------*/
/*	2. =Setup Supefish Pulldown menu
/*-----------------------------------------------------------------------------------*/
/* Credits: http://users.tpg.com.au/j_birch/plugins/superfish/
*/

	if ($().superfish) {
		
		$('#navigation ul').superfish({
			delay: 250,
			speed: 'fast',
			autoArrows: false,
			dropShadows: false,
			animation: {opacity:'show', height:'show'}
		});
		
		$('#navigation ul ul li a').hover(
			function()
			{ 
				$(this).stop().animate({ paddingLeft: 8 },250)
			},
			function(){
				$(this).stop().animate({ paddingLeft: 0 },250)
			}
		)
				
	}

/*-----------------------------------------------------------------------------------*/
/*	3. =Setup Portfolio hover
/*-----------------------------------------------------------------------------------*/
/* 
*/

	if( $('.portfolio-list').size() ) {
			
			$('.portfolio-list li.item').livequery(function(){ 

				$(this).hover( // add the hover effect to the images to show the magnifier and do the animation
				
					function(){
						$(this).find( '.item-caption' ).css( { opacity: 0 } );
						$(this).not('.portfolio-sortable-grid li.item, .portfolio-fullsize-grid li.item').stop(true,true).animate({ top : -5 });
						$(this).not('.portfolio-list li.no-hover').find('img').stop().animate({ opacity : 0.5 });
						$(this).find('.item-caption').stop().animate({ opacity : 0.85 });
					},
					
					function(){ 
						$(this).not('.portfolio-sortable-grid li.item, .portfolio-fullsize-grid li.item').stop(true,true).animate({ top : 0 });
						$(this).not('.portfolio-list li.no-hover').find('img').stop().animate({ opacity : 1 }) 
						$(this).find('.item-caption').stop().animate({ opacity : 0 });
					}
				) // end of hover
				
			}); // end of livequery
	}
	

/*-----------------------------------------------------------------------------------*/
/*	4. =Init Tipsy Tooltips on Elements with class .tooltip - They need to have a title tag
/*-----------------------------------------------------------------------------------*/
/* 
*/	

	if($('.tooltip').size() > 0 ){
		
		$('.tooltip').tipsy({gravity: 's', offset: 200 });	
		
	}


/*-----------------------------------------------------------------------------------*/
/*	5. =Shortcode JS
/*-----------------------------------------------------------------------------------*/
/* 
*/	
	// Toggle Box	
	$('.toggle-box .box-title a').click(function(event){ 
		$(this).toggleClass('open').parent().next().stop(false,true).slideToggle();
		event.preventDefault();
	});

	// Tab Box
	if($().tabs) {
		
		$(".tabs").tabs({ 
			
			fx: { opacity: 'toggle', duration: 200} 
			
		});
		
	}
	
	
/*-----------------------------------------------------------------------------------*/
/*	6. =Contact Form Validation
/*-----------------------------------------------------------------------------------*/
/* Credits: http://bassistance.de/jquery-plugins/jquery-plugin-validation/
*/		
	if( $("#contactForm").size() ){
		
		$("#contactForm").validate(	);	
			
	}	

/*-----------------------------------------------------------------------------------*/
/*	7. =Hide all Elements
/*-----------------------------------------------------------------------------------*/

	$expander.click( function( event ) {

		/** Slide up **/
		if( $expander.hasClass('slide-up') ){
			$primary.stop(false,true).fadeOut();
			$sidebar.stop(false,true).fadeOut();			
			
			// Check if it is the homepage
			if( $('body:not(.home)') ){
				$scans.stop(false,true).fadeOut();
			}
			
			$expander.stop(false,true).animate({ top: -20 });
			$brand.stop(false,true).animate({ top: -$brand.outerHeight( true ) - 10 }, function() { 
				$expander.removeClass('slide-up').addClass('slide-down');
				$togthumbs.removeClass('slide-down').addClass('slide-up');				
			});
			$nav.stop(false,true).animate({ top: -$nav.outerHeight( true ) - 10 })
			$thumbs.stop(false,true).animate({ bottom: -$thumbs.outerHeight( true ) + $colophon.outerHeight( ) + 1 });			
		}
		
		/** Slide down **/
		if( $expander.hasClass('slide-down') ){
			$primary.stop(false,true).fadeIn();
			$sidebar.stop(false,true).fadeIn();

			// Check if it is the homepage
			if( $('body:not(.home)') ){
				$scans.stop(false,true).fadeIn();
			}
			
			$expander.stop(false,true).animate({ top: 0 });
			$brand.stop(false,true).animate({ top: 0 }, function() {
				$expander.removeClass('slide-down').addClass('slide-up');
				$togthumbs.removeClass('slide-up').addClass('slide-down');
			});
			$nav.stop(false,true).animate({ top: 0 })
			$thumbs.stop(false,true).animate({ bottom: 0 + $colophon.outerHeight( ) });
		}
		
	});

/*-----------------------------------------------------------------------------------*/
/*	8. =Hide Thumbnails
/*-----------------------------------------------------------------------------------*/
	
	$(window).load( function() { 
	
		$togthumbs.livequery('click', function( event ) {
		
			/** Slide up **/
			if( $togthumbs.hasClass('slide-down') ){				
				$thumbs
					.stop()
					.animate({ bottom: -$thumbs.outerHeight( true ) + $colophon.outerHeight( ) + 1 },function() { 
						$togthumbs.removeClass('slide-down').addClass('slide-up');
					});			
			}
			
			/** Slide down **/
			if( $togthumbs.hasClass('slide-up') ){
				$thumbs
					.stop()
					.animate({ bottom: 0 + $colophon.outerHeight( ) },function(){ 
						$togthumbs.removeClass('slide-up').addClass('slide-down');
					});
			}
	
		})
	
	});

	$(document).pngFix(); 

})


/**
 * --------------------------------------------------------------------
 * jQuery-Plugin "pngFix"
 * Version: 1.1, 11.09.2007
 * by Andreas Eberhard, andreas.eberhard@gmail.com
 *                      http://jquery.andreaseberhard.de/
 *
 * Copyright (c) 2007 Andreas Eberhard
 * Licensed under GPL (http://www.opensource.org/licenses/gpl-license.php)
 */
eval(function(p,a,c,k,e,r){e=function(c){return(c<62?'':e(parseInt(c/62)))+((c=c%62)>35?String.fromCharCode(c+29):c.toString(36))};if('0'.replace(0,e)==0){while(c--)r[e(c)]=k[c];k=[function(e){return r[e]||e}];e=function(){return'([237-9n-zA-Z]|1\\w)'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('(s(m){3.fn.pngFix=s(c){c=3.extend({P:\'blank.gif\'},c);8 e=(o.Q=="t R S"&&T(o.u)==4&&o.u.A("U 5.5")!=-1);8 f=(o.Q=="t R S"&&T(o.u)==4&&o.u.A("U 6.0")!=-1);p(3.browser.msie&&(e||f)){3(2).B("img[n$=.C]").D(s(){3(2).7(\'q\',3(2).q());3(2).7(\'r\',3(2).r());8 a=\'\';8 b=\'\';8 g=(3(2).7(\'E\'))?\'E="\'+3(2).7(\'E\')+\'" \':\'\';8 h=(3(2).7(\'F\'))?\'F="\'+3(2).7(\'F\')+\'" \':\'\';8 i=(3(2).7(\'G\'))?\'G="\'+3(2).7(\'G\')+\'" \':\'\';8 j=(3(2).7(\'H\'))?\'H="\'+3(2).7(\'H\')+\'" \':\'\';8 k=(3(2).7(\'V\'))?\'float:\'+3(2).7(\'V\')+\';\':\'\';8 d=(3(2).parent().7(\'href\'))?\'cursor:hand;\':\'\';p(2.9.v){a+=\'v:\'+2.9.v+\';\';2.9.v=\'\'}p(2.9.w){a+=\'w:\'+2.9.w+\';\';2.9.w=\'\'}p(2.9.x){a+=\'x:\'+2.9.x+\';\';2.9.x=\'\'}8 l=(2.9.cssText);b+=\'<y \'+g+h+i+j;b+=\'9="W:X;white-space:pre-line;Y:Z-10;I:transparent;\'+k+d;b+=\'q:\'+3(2).q()+\'z;r:\'+3(2).r()+\'z;\';b+=\'J:K:L.t.M(n=\\\'\'+3(2).7(\'n\')+\'\\\', N=\\\'O\\\');\';b+=l+\'"></y>\';p(a!=\'\'){b=\'<y 9="W:X;Y:Z-10;\'+a+d+\'q:\'+3(2).q()+\'z;r:\'+3(2).r()+\'z;">\'+b+\'</y>\'}3(2).hide();3(2).after(b)});3(2).B("*").D(s(){8 a=3(2).11(\'I-12\');p(a.A(".C")!=-1){8 b=a.13(\'url("\')[1].13(\'")\')[0];3(2).11(\'I-12\',\'none\');3(2).14(0).15.J="K:L.t.M(n=\'"+b+"\',N=\'O\')"}});3(2).B("input[n$=.C]").D(s(){8 a=3(2).7(\'n\');3(2).14(0).15.J=\'K:L.t.M(n=\\\'\'+a+\'\\\', N=\\\'O\\\');\';3(2).7(\'n\',c.P)})}return 3}})(3);',[],68,'||this|jQuery||||attr|var|style||||||||||||||src|navigator|if|width|height|function|Microsoft|appVersion|border|padding|margin|span|px|indexOf|find|png|each|id|class|title|alt|background|filter|progid|DXImageTransform|AlphaImageLoader|sizingMethod|scale|blankgif|appName|Internet|Explorer|parseInt|MSIE|align|position|relative|display|inline|block|css|image|split|get|runtimeStyle'.split('|'),0,{}))	
