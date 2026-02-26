import gdsfactory as gf
gf.gpdk.PDK.activate()  # Activate the generic silicon photonics PDK

dc = gf.components.coupler(length=5.0, gap=0.2)

# Save the component as a GDS file
dc.write_gds("si_2x2_50_50_beamsplitter_DC.gds")

