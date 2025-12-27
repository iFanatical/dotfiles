import XMonad
import XMonad.Util.EZConfig (additionalKeysP)
import XMonad.Layout.Spacing
import XMonad.Layout.Renamed
import XMonad.Hooks.DynamicLog
import XMonad.Hooks.StatusBar
import XMonad.Hooks.StatusBar.PP
import XMonad.Hooks.ManageDocks

-- TokyoNight Colors
colorBg = "#1a1b26" -- background
colorFg = "#a9b1d6" -- foreground
colorBlk = "#32344a" -- black
colorRed = "#f7768e" -- red
colorGrn = "#9ece6a" -- green
colorYlw = "#e0af68" -- yellow
colorBlu = "#7aa2f7" -- blue
colorMag = "#ad8ee6" -- magenta
colorCyn = "#0db9d7" -- cyan
colorBrBlk = "#444b6a" -- bright black

-- Appearance
myBorderWidth = 2
myNormalBorderColor = colorBrBlk
myFocusedBorderColor = colorMag
mySpacing = spacingWithEdge 2

-- Workspaces
myWorkspaces = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

-- Programs
myTerminal = "kitty"
myBrowser = "brave"
myBrowser2 = "firefox"
myRunner = "$HOME/.config/rofi/launchers/type-1/launcher.sh"

myLayoutHook = avoidStruts $ spacingWithEdge 2 $ layoutHook def

myXmobarPP :: PP
myXmobarPP = def
    { ppCurrent = xmobarColor "#0db9d7" ""
    , ppHidden = xmobarColor "#a9b1d6" ""
    , ppHiddenNoWindows = xmobarColor "#444b6a" ""
    }

myStatusBar = statusBarProp "xmobar" (pure myXmobarPP)

myKeys =
    [ ("M-<Return>", spawn myTerminal)
    , ("M-d", spawn myRunner)
    , ("M-w", spawn "fanos-menu")
    , ("M-b", spawn myBrowser)
    , ("M-S-b", spawn myBrowser2)
    , ("M-S-r", spawn "xmonad --recompile && xmonad --restart")
    , ("M-S-c", kill)
    , ("M-S-<Backspace>", spawn "pkill xmonad")
    ]

myConfig =
    def
     { modMask = mod4Mask
     , terminal = "kitty"
     , borderWidth = 2
     , normalBorderColor = myNormalBorderColor
     , focusedBorderColor = myFocusedBorderColor
     , layoutHook = myLayoutHook
     }
     `additionalKeysP` myKeys

main :: IO ()
main = xmonad $ withEasySB myStatusBar defToggleStrutsKey $ myConfig
