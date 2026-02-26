import gdsfactory as gf
gf.gpdk.PDK.activate()  # Activate the generic silicon photonics PDK

mmi = gf.components.mmi2x2()

mmi.write_gds("si_2x2_50_50_beamsplitter_MMI.gds")
