import streamlit as st
import pandas as pd
import numpy as np
import io

st.set_page_config(page_title="Product Enrichment Tool")
st.title("Seasonal Product Enrichment Tool")
st.markdown("""
Upload your Excel file with the seasonal articles. This tool will automatically enrich missing fields based on name patterns
and provide a downloadable Excel file with the completed data.
""")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

def enrich_data(df):
    df = df.copy()
    
    # Create the new enriched column based on conditions
    df["Enriched Product Line"] = df.apply(lambda row: (
        "Agravic" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Agravic" in str(row.get("Name", "")) else
        "Samba;60s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Samba 62" in str(row.get("Name", "")) else
        "Superstar" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Superstar" in str(row.get("Name", "")) else
        "Freerider" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Freerider" in str(row.get("Name", "")) else
        "Aleon" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Aleon" in str(row.get("Name", "")) else
        "Crawe" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Crawe" in str(row.get("Name", "")) else
        "Hellcat" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Hellcat" in str(row.get("Name", "")) else
        "Hiangle" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Hiangle" in str(row.get("Name", "")) else
        "Kestrel" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Kestrel" in str(row.get("Name", "")) else
        "Kirigami" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Kirigami" in str(row.get("Name", "")) else
        "NIAD" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten NIAD" in str(row.get("Name", "")) else
        "Sleuth" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Sleuth" in str(row.get("Name", "")) else
        "Trailcross" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Trailcross" in str(row.get("Name", "")) else
        "Adventure" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["Adventure", "Hyperturf", "Mocaturf", "Roverend", "Rovermule", "Superturf"]) else
        "Astir;2000s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Astir" in str(row.get("Name", "")) else
        "Campus" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Campus" in str(row.get("Name", "")) else
        "Forum" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Forum" in str(row.get("Name", "")) else
        "Gazelle;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Gazelle" in str(row.get("Name", "")) else
        "Nizza" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Nizza" in str(row.get("Name", "")) else
        "NMD" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "NMD" in str(row.get("Name", "")) else
        "Oz;2000s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Oz " in str(row.get("Name", "")) else
        "Samba;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Samba" in str(row.get("Name", "")) and "Cycling" not in str(row.get("Name", "")) else
        "Shmoofoil" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Shmoofoil" in str(row.get("Name", "")) else
        "Stan Smith" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Stan Smith" in str(row.get("Name", "")) else
        "Adilette" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Puffylette" in str(row.get("Name", "")) else
        "Adifom" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adifom Supernova" in str(row.get("Name", "")) else
        "adilette" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "adilette" in str(row.get("Name", "")) else
        "adizero" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["adizero", "Jumpstar", "DistanceStar", "Ubersonic 4", "Sprintstar", "Throwstar"]) else
        "Aeroimpact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Aeroimpact" in str(row.get("Name", "")) else
        "Alphaboost" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["alphaboost", "alphaboost V1"]) else
        "Copa" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Copa" in str(row.get("Name", "")) else
        "Fast Impact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Fast Impact" in str(row.get("Name", "")) else
        "Optime" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Optime" in str(row.get("Name", "")) else
        "Own the Run" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["OTR", "Own the Run"]) else
        "Power Impact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Power Impact" in str(row.get("Name", "")) else
        "Powerreact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Powerreact" in str(row.get("Name", "")) else
        "Predator" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Predator" in str(row.get("Name", "")) else
        "Tiro" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tiro" in str(row.get("Name", "")) else
        "Purelounge" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Purelounge" in str(row.get("Name", "")) else
        "Solar" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["Solarboost", "Solarcontrol", "Solarglide", "Solarmotion"]) else
        "Supernova" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Supernova" in str(row.get("Name", "")) else
        "Ultraboost" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ultraboost" in str(row.get("Name", "")) else
        "4DFWD" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "4DFWD" in str(row.get("Name", "")) else
        "Hellcat" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Hellcat" in str(row.get("Name", "")) else
        "Freerider" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Freerider" in str(row.get("Name", "")) else
        "Aleon" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Aleon" in str(row.get("Name", "")) else
        "Crawe" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Crawe" in str(row.get("Name", "")) else
        "Agravic Speed" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Agravic Speed Ultra" in str(row.get("Name", "")) else
        "AX4" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX AX4" in str(row.get("Name", "")) else
        "Eastrail" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Eastrail" in str(row.get("Name", "")) else
        "Free Hiker" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Free Hiker" in str(row.get("Name", "")) else
        "Skychaser" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Skychaser" in str(row.get("Name", "")) else
        "Swift" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Swift" in str(row.get("Name", "")) else
        "Techrock" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Techrock" in str(row.get("Name", "")) else
        "Voyager" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Voyager" in str(row.get("Name", "")) else
        "Xperior" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Xperior" in str(row.get("Name", "")) else
        "Xploric" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Xploric" in str(row.get("Name", "")) else
        "Coreflow" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Coreflow Studio" in str(row.get("Name", "")) or "Coreflow Luxe" in str(row.get("Name", ""))) else
        "Cloudfoam Pure" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Cloudfoam Pure" in str(row.get("Name", "")) else
        "CodeChaos" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Codechaos" in str(row.get("Name", "")) else
        "Cross Em" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Cross Em" in str(row.get("Name", "")) else
        "D.O.N" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["DON", "D.O.N Issue 5", "D.O.N Issue 6", "D.O.N Issue 7", "D.O.N Issue 8"]) else
        "Designed for Training" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Designed for Training" in str(row.get("Name", "")) else
        "Exhibit" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Exhibit" in str(row.get("Name", "")) else
        "Go-To" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Go-To" in str(row.get("Name", "")) else
        "Impact FLX" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Impact FLX" in str(row.get("Name", "")) else
        "Lillard;Dame" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Dame 8" in str(row.get("Name", "")) or "Dame" in str(row.get("Name", ""))) else
        "MC80" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "MC80" in str(row.get("Name", "")) else
        "MC87" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "MC87" in str(row.get("Name", "")) else
        "Retrocross" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Retrocross" in str(row.get("Name", "")) else
        "S2G" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "S2G" in str(row.get("Name", "")) else
        "Soulstride" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Soulstride" in str(row.get("Name", "")) else
        "Swift Run" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Swift Run" in str(row.get("Name", "")) else
        "Teamwear" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in [
            "Atlanta United", "Austin FC", "CF Montreal", "Charlotte FC", "Chicago Fire", "Colorado Rapids", "Columbus Crew", "D.C. United",
            "FC Cincinnati", "FC Dallas", "Houston Dynamo", "Inter Miami CF", "LA Galaxy", "LAFC", "Los Angeles Football Club",
            "Manchester United", "Minnesota United", "Nashville SC", "New England Revolution", "New York City FC",
            "New York Red Bulls", "Orlando City", "Orlando City SC", "Philadelphia Union", "Portland Timbers", "Real Salt Lake",
            "San Jose Earthquakes", "Seattle Sounders", "Seattle Sounders FC", "Sporting Kansas City", "St. Louis CITY FC",
            "ST Louis City SC", "Toronto FC", "Vancouver Whitecaps", "Jamaica Beckenbauer", "Lightning Third",
            "Washington Huskies", "AFC Ajax", "Benfica", "Celtic FC", "FC Bayern Munich", "Newcastle United FC",
            "Olympique Lyonnais", "Arsenal", "Juventus", "Real Madrid"
        ]) else
        "Trailmaker" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Trailmaker" in str(row.get("Name", "")) else
        "TrueCasuals" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TrueCasuals" in str(row.get("Name", "")) else
        "TruePace" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TruePace" in str(row.get("Name", "")) else
        "Ultimate365" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ultimate365" in str(row.get("Name", "")) else
        "ZG" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("ZG23" in str(row.get("Name", "")) or "ZG21" in str(row.get("Name", ""))) else
        "Zoysia" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Zoysia" in str(row.get("Name", "")) else
        "Trae" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Trae" in str(row.get("Name", "")) or "Trae Unlimited" in str(row.get("Name", ""))) else
        "Ultraboost" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ultraboost light" in str(row.get("Name", "")) else
        "Tiro" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TIRO24" in str(row.get("Name", "")) else
        "Copa" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Copa Gloro" in str(row.get("Name", "")) else
        "True Purpose" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TruePurpose" in str(row.get("Name", "")) else
        "Response" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Response" in str(row.get("Name", "")) else
        "Daily" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Daily" in str(row.get("Name", "")) else
        "Impact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Five Ten Impact" in str(row.get("Name", "")) or "Five Ten" in str(row.get("Name", ""))) else
        "Futurecraft" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Futurecraft" in str(row.get("Name", "")) else
        "Run 70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Run 70s Shoes" in str(row.get("Name", "")) else
        "Run 80s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Run 80s Shoes" in str(row.get("Name", "")) else
        "Earthlight" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Earthlight" in str(row.get("Name", "")) else
        "Eastrail" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Eastrail" in str(row.get("Name", "")) else
        "VULCRAID3R" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "VULCRAID3R" in str(row.get("Name", "")) else
        "Sport Pro" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "adidas x LEGO® Sport Pro Running Shoes" in str(row.get("Name", "")) else
        "Questar" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Questar" in str(row.get("Name", "")) else
        "Tensaur" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tensaur" in str(row.get("Name", "")) else
        "Summervent" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Summervent" in str(row.get("Name", "")) else
        "Puig" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Puig" in str(row.get("Name", "")) else
        "CourtJam" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "CourtJam" in str(row.get("Name", "")) else
        "Avacourt" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Avacourt" in str(row.get("Name", "")) else
        "Tracefinder" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tracefinder" in str(row.get("Name", "")) else
        "QT Racer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "QT Racer" in str(row.get("Name", "")) else
        "Start Your Run" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Start Your Run" in str(row.get("Name", "")) else
        "Activeride" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Activeride 2.0" in str(row.get("Name", "")) else
        "ZNCHILL" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZNCHILL" in str(row.get("Name", "")) else
        "Solarmotion" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Solarmotion" in str(row.get("Name", "")) else
        "Kantana" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Kantana Shoes" in str(row.get("Name", "")) else
        "Midcity" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Midcity Low Shoes" in str(row.get("Name", "")) else
        "Winterplay" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Winterplay" in str(row.get("Name", "")) else
        "X" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "X League" in str(row.get("Name", "")) else
        "Retro" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["Retro Graphic", "Retro Quarter"]) else
        "RDY" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["COLD.RDY", "HEAT.RDY", "RAIN.RDY", "SUMMER.RDY", "WIND.RDY"]) else
        "Top Ten" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Top Ten" in str(row.get("Name", "")) else
        "Spezial;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and pd.notna(row.get("PIM - Label")) and "Originals" in str(row.get("PIM - Label", "")) and "Handball Spezial" in str(row.get("Name", "")) else
        "Tyshawn" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tyshawn" in str(row.get("Name", "")) else
        "adiFOM;Stan Smith" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adifom Stan Smith" in str(row.get("Name", "")) else
        "adilette;adiFOM" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adifom Adilette" in str(row.get("Name", "")) else
        "adiFOM" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "adiFOM" in str(row.get("Name", "")) else
        "BYW Select" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "BYW Select" in str(row.get("Name", "")) else
        "ADI2000" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ADI2000" in str(row.get("Name", "")) else
        "Matchbreak" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Matchbreak" in str(row.get("Name", "")) else
        "Crazy" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Crazy" in str(row.get("Name", "")) else
        "Crazyflight" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Crazyflight" in str(row.get("Name", "")) else
        "Adibreak" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adibreak" in str(row.get("Name", "")) else
        "Select" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Select" in str(row.get("Name", "")) else
        "All Me" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "All Me " in str(row.get("Name", "")) else
        "Designed for Training" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["D4T", "Designed-for-Training"]) else
        "SL 72;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "SL 72" in str(row.get("Name", "")) else
        "Country;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Country" in str(row.get("Name", "")) else
        "Retropy;2000s;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Retropy" in str(row.get("Name", "")) else
        "adicolor;Beckenbauer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in [
            "Arsenal Beckenbauer", "Real Madrid Beckenbauer", "Juventus Beckenbauer", "Adicolor Classics Beckenbauer"
        ]) else
        "adicolor;VRCT" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adicolor VRCT" in str(row.get("Name", "")) else
        "Beckenbauer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Beckenbauer" in str(row.get("Name", "")) else
        "3MC" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "3MC" in str(row.get("Name", "")) else
        "adicolor" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adicolor" in str(row.get("Name", "")) else
        "Adimatic" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adimatic" in str(row.get("Name", "")) else
        "Adipower" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adipower" in str(row.get("Name", "")) else
        "Adistar" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adistar" in str(row.get("Name", "")) else
        "Avaflash" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Avaflash" in str(row.get("Name", "")) else
        "AVRYN" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Avryn_X" in str(row.get("Name", "")) else
        "Barricade" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Barricade" in str(row.get("Name", "")) else
        "Busenitz" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Busenitz" in str(row.get("Name", "")) else
        "Dropset" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Dropset" in str(row.get("Name", "")) else
        "Galaxy" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Galaxy" in str(row.get("Name", "")) else
        "Harden" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Harden" in str(row.get("Name", "")) else
        "Hoops" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Hoops" in str(row.get("Name", "")) else
        "Icon" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Icon" in str(row.get("Name", "")) else
        "Matchbreak Super" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Matchbreak Super" in str(row.get("Name", "")) else
        "MYSHELTER" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "MYSHELTER" in str(row.get("Name", "")) else
        "Powerlift" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Powerlift" in str(row.get("Name", "")) else
        "Pureboost" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Pureboost" in str(row.get("Name", "")) else
        "Rapida" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "RapidaSport" in str(row.get("Name", "")) else
        "Rivalry" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Rivalry" in str(row.get("Name", "")) else
        "Sereno" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Sereno" in str(row.get("Name", "")) else
        "Stabil" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Stabil" in str(row.get("Name", "")) else
        "Tango" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tango" in str(row.get("Name", "")) else
        "Tour360" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tour360" in str(row.get("Name", "")) else
        "ZX" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZX" in str(row.get("Name", "")) else
        "adicross" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "adicross" in str(row.get("Name", "")) else
        "ZPLAASH" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZPLAASH" in str(row.get("Name", "")) else
        "adibreak" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ADBRK" in str(row.get("Name", "")) else
        "Lacombe" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Lacombe" in str(row.get("Name", "")) else
        "Hoop York City" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["HYC", "Hoop York City"]) else
        "ZNE" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZNE" in str(row.get("Name", "")) else
        "Koln" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Koln" in str(row.get("Name", "")) else
        "Munchen" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Munchen" in str(row.get("Name", "")) else
        "The Total" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "The Total" in str(row.get("Name", "")) else
        "Amplimove" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Amplimove" in str(row.get("Name", "")) else
        "Velostan" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Velostan" in str(row.get("Name", "")) else
        "Novaflight" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Novaflight" in str(row.get("Name", "")) else
        "VRCT" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "VRCT" in str(row.get("Name", "")) else
        "Gamemode" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Gamemode" in str(row.get("Name", "")) else
        "Goletto" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Goletto" in str(row.get("Name", "")) else
        "Anthony Edwards" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Anthony Edwards" in str(row.get("Name", "")) else
        "D.O.N" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "D.O.N" in str(row.get("Name", "")) else
        "Megaride;2000s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Megaride" in str(row.get("Name", "")) else
        "Centennial" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Centennial" in str(row.get("Name", "")) else
        "Aloha Super" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Aloha Super" in str(row.get("Name", "")) else
        "adizero" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Takumi Sen" in str(row.get("Name", "")) else
        "Helionic" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Helionic" in str(row.get("Name", "")) else
        "Alphaskin" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Alphaskin" in str(row.get("Name", "")) else
        "Anylander" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Anylander" in str(row.get("Name", "")) else
        "Xperior" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Xperior" in str(row.get("Name", "")) else
        "EQT" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Equipment" in str(row.get("Name", "")) or "EQT" in str(row.get("Name", ""))) else
        "Dugout" if pd.isna(row.get("PIM - Product Line (sportsub)")) and (
            "Baseball" in str(row.get("PIM - Sport", "")) or "Softball" in str(row.get("PIM - Sport", ""))
        ) else
        "Beyond the Course" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Golf" in str(row.get("PIM - Sport", "")) and "Beyond" in str(row.get("Name", "")) else
        "CodeChaos" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Golf" in str(row.get("PIM - Sport", "")) and "Codechaos" in str(row.get("Name", "")) else
        "Clima" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Clima" in str(row.get("Name", "")) else
        "Everyset" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Everyset" in str(row.get("Name", "")) else
        "Rapidmove" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Rapidmove" in str(row.get("Name", "")) else
        "Stella Court" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Stella McCartney Court" in str(row.get("Name", "")) else
        "GameCourt" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Gamecourt" in str(row.get("Name", "")) else
        "Solematch" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Solematch" in str(row.get("Name", "")) else
        "TLDR" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TLDR" in str(row.get("Name", "")) else
        "Coursecup" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Coursecup" in str(row.get("Name", "")) else
        "Gym+" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Gym+" in str(row.get("Name", "")) else
        "Pacer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Pacer" in str(row.get("Name", "")) else
        "Designed for Training" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Designed-for-Training" in str(row.get("Name", "")) else
        "Run 70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Run 70s" in str(row.get("Name", "")) else
        "Lightblaze " if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Lightblaze" in str(row.get("Name", "")) else
        "ZNSORY" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZNSORY" in str(row.get("Name", "")) else
        "Aspyre" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Aspyre" in str(row.get("Name", "")) else
        "BRMD" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "BRMD" in str(row.get("Name", "")) else
        "Ultradream" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ultradream" in str(row.get("Name", "")) else
        "ZNE" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Soccer" in row.get("PIM - Sport", '') and "Z.N.E" in str(row.get("Name", "")) else
        "Spezialist" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Spezialist" in str(row.get("Name", "")) else
        "Ligra" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ligra" in str(row.get("Name", "")) else
        "Essentials" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Essentials" in str(row.get("Name", "")) else
        "Worldwide Hoops" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Worldwide Hoops" in str(row.get("Name", "")) or "WWH " in str(row.get("Name", ""))) else
        "adilenium" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adilenium" in str(row.get("Name", "")) else
        "Teamwear" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(team in str(row.get("Name", "")) or team in str(row.get("PIM - Teams", "")) for team in [
            "University of Louisville", "Louisville Cardinals", "Texas A&M", "Texas A&M Aggies", "University of Kansas", "Kansas Jayhawks",
            "University of Miami", "Miami Hurricanes", "University of Nebraska", "Nebraska Cornhuskers",
            "North Carolina State University", "North Carolina", "Arizona State University", "Grambling State University", "Grambling State Tigers",
            "Indiana University", "Indiana Hoosiers", "University of Washington", "Washington Huskies", "NC State", "NC State Wolfpack",
            "New Zealand Rugby", "All Blacks", "Texas Tech", "Hoosiers", "Huskies", "Georgia Tech", "Yellow Jackets",
            "Alcorn State", "Alcorn State Braves", "Arkansas Pine Bluff", "Arkansas-Pine Bluff Golden Lions",
            "Mississippi State University", "Mississippi State Bulldogs", "Alabama State", "Alabama State Hornets",
            "Black History Month University"
        ]) else
        "Initiation" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Initiation" in str(row.get("Name", "")) else
        "BB Legends" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Basketball Legends" in str(row.get("Name", "")) else
        "Crazy Lite" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Crazy lite" in str(row.get("Name", "")) else
        "Ballerina" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ballerina" in str(row.get("Name", "")) else
        "Palos Hills" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Palos Hills" in str(row.get("Name", "")) else
        "Seeulater" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Seeulater" in str(row.get("Name", "")) else
        "Superskate" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Superskate" in str(row.get("Name", "")) else
        "Italia" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Italia" in str(row.get("Name", "")) else
        "Montreal" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Montreal" in str(row.get("Name", "")) else
        "Adiraptor" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adiraptor" in str(row.get("Name", "")) else
        "Ghost Sprint" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ghost Sprint" in str(row.get("Name", "")) else
        "Feroza" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Motorsport" in str(row.get("PIM - Sport", "")) and "Feroza" in str(row.get("Name", "")) else
        "Adiracer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Motorsport" in str(row.get("PIM - Sport", "")) and "Adiracer" in str(row.get("Name", "")) else
        "Heritage" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tennis" in str(row.get("PIM - Sport", "")) and "Heritage" in str(row.get("Name", "")) else
        "Defiant Speed" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tennis" in str(row.get("PIM - Sport", "")) and "Defiant" in str(row.get("Name", "")) else
        row.get("PIM - Product Line (sportsub)")
    ), axis=1)
    
    return df

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        enriched_df = enrich_data(df)

        # Show preview
        st.success("File processed successfully! Here's a preview:")
        st.dataframe(enriched_df.head())

        # Convert to Excel for download
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            enriched_df.to_excel(writer, index=False)
        
        st.download_button(
            label="📥 Download Enriched Excel",
            data=output.getvalue(),
            file_name="enriched_products.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as e:
        st.error(f"There was an error processing the file: {e}")

