CoordMode Pixel  ; Interprets the coordinates below as relative to the screen rather than the 

Loop,
{
   ; first two store the found position, next 4 as the search area in pixels, then the file.
   ImageSearch, OutputVarX, OutputVarY, 0, 0, A_ScreenWidth, A_ScreenHeight, ./popcap.png

   ; "0" means no match
   if (OutputVarX > 0) { 
      Run, python ./splogin.py -u 0 -c E0049149C2CEBD90 --password xxx,, hide
	  sleep, 10000
   }

   sleep, 1000 
} 