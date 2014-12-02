\* tofu *\
Maximize
OBJ: 12 edamame_flavored_rt + 4 edamame_fresh + 7 edamame_fresh_flavored_ot
 + 13 tempeh_flavored_rt + 4 tempeh_fresh + 9 tempeh_fresh_flavored_ot
 + 14 tofu_flavored_rt + 8 tofu_fresh + 11 tofu_fresh_flavored_ot
Subject To
EdamameAmmountRequirement: edamame_flavored_rt + edamame_fresh
 + edamame_fresh_flavored_ot = 400
FlavoringOvertimeRequirement: edamame_fresh_flavored_ot
 + tempeh_fresh_flavored_ot + tofu_fresh_flavored_ot <= 250
FlavoringRegularTimeRequirement: edamame_flavored_rt + tempeh_flavored_rt
 + tofu_flavored_rt <= 420
TempehAmmountRequirement: tempeh_flavored_rt + tempeh_fresh
 + tempeh_fresh_flavored_ot = 230
TofuAmmountRequirement: tofu_flavored_rt + tofu_fresh + tofu_fresh_flavored_ot
 = 480
Bounds
0 <= edamame_flavored_rt
0 <= edamame_fresh
0 <= edamame_fresh_flavored_ot
0 <= tempeh_flavored_rt
0 <= tempeh_fresh
0 <= tempeh_fresh_flavored_ot
0 <= tofu_flavored_rt
0 <= tofu_fresh
0 <= tofu_fresh_flavored_ot
Generals
edamame_flavored_rt
edamame_fresh
edamame_fresh_flavored_ot
tempeh_flavored_rt
tempeh_fresh
tempeh_fresh_flavored_ot
tofu_flavored_rt
tofu_fresh
tofu_fresh_flavored_ot
End
