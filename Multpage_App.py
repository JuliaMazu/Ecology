import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import folium
#from streamlit_folium import st_folium
import plotly.express as px

#dataframe
df_global_temp = pd.read_csv('global_temperature')
df_disaster = pd.read_csv('disaster')
df_dis = pd.DataFrame({'Types' : ['Droughts', 'Droughts', 'Earthquakes', 'Earthquakes', 'Extreme temperature', 'Extreme temperature', 'Floods', 'Floods', 'Storms', 'Storms'], 'Number of events' : [6,9,27, 35, 28, 41, 141, 235, 97, 99], 'Decade' : ['1985–97','1998–2009', '1985–97','1998–2009', '1985–97', '1998–2009', '1985–97','1998–2009', '1985–97', '1998–2009']})
df_glasier = pd.read_csv('glacier')
df_sea_level = pd.read_csv('sea level')
df_volcan = pd.read_csv('volcans')
df_volcan['Coordinates'] = df_volcan['Coordinates'].apply(lambda x: x.split(','))
df_sunspot = pd.read_csv('sunspot')
df_CO2_temp = pd.read_csv('CO2 emmition')
df_pour_ML = pd.read_csv('gazes and temperature')
df_ML = pd.read_csv('the last')
df_ML.set_index('year', inplace=True)
df_ML.drop(columns='Unnamed: 0', inplace=True)
list_importance = [0.16807112, 0.01082996, 0.02037711, 0.10149383, 0.69922798]
feature = ['Radiation', 'Volcanic Emmision','CO2 W m2', 'CH4 W m2', 'N2O W m2']

df_gazes = pd.DataFrame({'Greenhouse Gases' : ['Carbon dioxide', 'Methane', 'Nitrous oxide', 'Tropospheric ozone', 'CFC-12', 'HCFC-22', 'Sulfur hexaflouride'],
'Chemical Formulae' : ['CO2', 'CH4', 'N2O', 'O3', 'CCL2F2', 'CCl2F2', 'SF6'],
'Anthropogenic Sources' : ['Fossil-fuel combustion, land-use conversion, cement', 'Fossil fuels, rice paddies, waste dumps',  'Fertilizer, industrial processes, combustion', 'Fossil fuel combustion, industrial emissions, chemical solvents', 'Liquid coolants, foams', 'Refrigerant', 'Dielectric fluid'],
'Atmospheric Lifetime (Years)' : [100, 12, 144, 0, 100, 12, 3200]})

df_disaster_reported = pd.read_csv('disaster_by_year')

#streamlit function
def intro():
    st.markdown("<h1 style='text-align: center; color: grey;'>What is the climate change and does it affect me?</h1>", unsafe_allow_html=True)

    st.write("The philosophy of climate change rests on the global energy balance and emission scenario. The balance is expressed as the difference between the total energy received from the Sun, against the sum of energy reflected by the clouds, and that absorbed by the Earth and the atmosphere. An imbalance of the above since the industrial revolution in the eighteenth century witnessed an unmatched increase in the concentration of greenhouse gases (GHG) in the atmosphere and the temperature of the planet Earth.")

    st.image("https://th.bing.com/th/id/R.ed6620f65408446280a4d7981cecf56f?rik=9AkNCtI3NgpkWw&riu=http%3a%2f%2fmedia.giphy.com%2fmedia%2fhE7qzzcOwXh5u%2fgiphy.gif&ehk=GsIgDb%2b5agex2GX5n9%2f8NkA32U6roLqG3Jvvwjdb%2fWw%3d&risl=&pid=ImgRaw&r=0")


def factors():    
    st.markdown("<h1 style='text-align: center; color: grey;'>Impact of climate change</h1>", unsafe_allow_html=True)

    st.write('Climate change is caused both by natural events and anthropogenic activities. We discuss these below')
    with st.container():
        option = st.selectbox(
            'There are different factors which shows us the climat change',
            ('', 'Temperature change', 'Natural disasters', 'Glacier melting', 'Change in sea level'))


        if option == 'Temperature change':
            viz_pair = sns.lineplot(df_global_temp, x = 'Year', y = 'Mean', palette='mako')
            st.write('The average surface temperature of the Earth rose by 0.74 ± 0.18°C over the period between 1906 and 2005')
            st.write('The largest increase in temperature occurs closer to the poles, especially in the Arctic, where snow and ice cover have decreased substantially ')
            st.markdown("<h6 style='text-align: right; color: grey;'>Source https://data.giss.nasa.gov/gistemp/</h6>", unsafe_allow_html=True)

        elif option == 'Natural disasters':
            with st.container():
                fig = px.bar(df_disaster, x = 'Year', y = 'total', title='Total number of death because of natural disaster')
                st.plotly_chart(fig)            
                st.write('It is estimated that on an average, globally, 0.8–1.1 million people per year are affected by flood. Rise in temperature leads to more evaporation causing increased rainfall and snowfall.')
                    
            with st.container():
                st.markdown("<h6 style='text-align: right; color: grey;'>Source Mukhopadhyay, Ranadhir (2018). Climate Change || Scientific Assessment</h6>", unsafe_allow_html=True)
                sns.set(font_scale=0.8)
                viz_pair1 = sns.barplot(df_dis, x = 'Types', y = 'Number of events', hue = 'Decade', palette='mako').set_title('Number of natural disaster in Asia by the last decades')
                st.pyplot(viz_pair1.figure)
                
        
        elif option == 'Glacier melting':
            st.write('The volume of ice in a glacier and correspondingly its surface area, thickness, and length is determined by the balance between inputs (accumulation of snow and ice) and  outputs (melting and calving). And the balance between inputs and outputs  is influenced by temperature, precipitation, humidity, wind speed, and other  factors such as slope and the reflectivity of the glacier surface')
            viz_pair = sns.lineplot(df_glasier, x = 'Year', y = 'Mean cumulative mass balance')
            st.markdown("<h6 style='text-align: right; color: grey;'>Source https://data.giss.nasa.gov/gistemp/</h6>", unsafe_allow_html=True)

        
        elif option == 'Change in sea level':
            st.write('The sea level rise is caused by widespread melting of snow and ice, as well as thermal expansion of sea water as it expands when it warmed above 3.98°C')
            viz_pair = sns.lineplot(df_sea_level, x = 'year', y = 'GMSL')
            st.markdown("<h6 style='text-align: right; color: grey;'>Source https://noaadata.apps.nsidc.org/</h6>", unsafe_allow_html=True)

 
        try:
            st.pyplot(viz_pair.figure)
        except: 
            pass

def guilty():
    st.markdown("<h1 style='text-align: center; color: grey;'>Causes of climate change</h1>", unsafe_allow_html=True)
    st.write('Climate change is caused both by natural events and anthropogenic activities')

    with st.container():
        option2 = st.selectbox(
            'Which has the biggest impact?',
            ('', 'Natural factors', 'Human impact'))
        if option2=='Natural factors':
            option1 = st.selectbox(
            'A number of natural factors influence the ocean and atmosphere periodically and greatly impact the climate. Few among these are drifts of continents, volcanic eruptions, ocean currents, variations in the Earth’s orbital characteristics and solar output',
            ('', 'Volcan', 'Sun radiation'))
            if option1=='Volcan':
                st.write('Volcanic eruptions and global warming are inextricably related since the formation of the Earth. This is because volcanoes have been spewing enormous amount of ash, water vapor, and green house gazes into the atmosphere.')
                st.markdown("<h6 style='text-align: right; color: grey;'>Source http://www.ngdc.noaa.gov/</h6>", unsafe_allow_html=True)

#               m = folium.Map(location=df_volcan['Coordinates'].iloc[0], zoom_start=7)
#              for i in range(len(df_volcan)):
#                        folium.Marker(
#                        location=df_volcan['Coordinates'].iloc[i],
#                        popup=str(df_volcan['Volcano Name'].iloc[i]) + '\n'+ str(df_volcan['Year'].iloc[i]) + '\n' + str(df_volcan['Volcanic Explosivity Index'].iloc[i])
#                        ).add_to(m) 
#                st_data = st_folium(m, width=725)
            if option1 == 'Sun radiation':
                st.write('Solar magnetic fields produce sunspots, whose number increases and decreases with a 10.7-year periodicity (Milankovitch Cycle). This puzzling regularity in the Sun activity is known as solar cycle. ')
                st.markdown("<h6 style='text-align: right; color: grey;'>Source https://www.sidc.be/SILSO/datafiles-old</h6>", unsafe_allow_html=True)
                viz_pair1 = sns.lineplot(df_sunspot, y = 'number of spots', x = 'year', palette = 'mako')
                st.pyplot(viz_pair1.figure)
        
        if option2=='Human impact':
            st.write('Host of evidences are emerging to suggest that human activity is the primary reason for recent warming. These assessments show that the recent rise in temperature is clearly unusual in at least during the last 1000 years, when no major variation in solar energy input had been noticed ')
            st.markdown("<h6 style='text-align: right; color: grey;'>Source CDIAC website</h6>", unsafe_allow_html=True)
            fig = px.bar(df_CO2_temp[df_CO2_temp['year']>1800], x="year", y=['Gas', 'Liquids', 'Solids', 'Production', 'Flaring'], color_discrete_map= {'Gas': 'black',
                                      'Liquids': 'grey',
                                      'Solids': 'blue',
                                      'Production': 'green',
                                      'Flaring': 'red'}, title = 'CO2 emmition from the different sources')
            st.plotly_chart(fig)
            st.write('Besides of CO2 there are other greenhouse gazes: methan, nitrous oxide, tropospheric ozone, CFC-12, HCFC-22, sulfur hexeflouride')
            df_gazes
            df = df_pour_ML.set_index('year')
            st.markdown("<h6 style='text-align: right; color: grey;'>Source https://earth.jpl.nasa.gov/</h6>", unsafe_allow_html=True)
            viz_pair = sns.lineplot(df[['CO2 W m2', 'CH4 W m2','N2O W m2']], palette='mako').set_title('Green house gazes emissions')
            st.pyplot(viz_pair.figure)

    
def impact():
    st.markdown("<h1 style='text-align: center; color: grey;'>Simulation of human impact with machine learning</h1>", unsafe_allow_html=True)
    
    with st.container():
        st.write('Machine learning (DTC) prediction of temperature anomaly responce driven by both human and natural factors, and by only natural drivers (solar and volcanic activity). Comparizon with the real data')

        viz_ML = sns.lineplot(df_ML, palette='Dark2').set_title('Changes in registred temperature anomaly over the past 270 years')
        st.pyplot(viz_ML.figure)
        st.markdown("<h6 style='text-align: right; color: grey;'>Source of temperature anomaly https://berkeleyearth.org/</h6>", unsafe_allow_html=True)

        
    with st.container():
        fig = px.bar(x = feature, y = list_importance, title='Importance of some features in the temperature anomaly')
        st.plotly_chart(fig)
        st.write('Human influence has likely increased the chance of temperature change since the 1950s. This includes increases in the frequency of concurrent heatwaves and droughts on the global scale, fire weather in some regions of all inhabited continents, and compound flooding in some locations')


    with st.container():
        
        viz = sns.heatmap(df_pour_ML[['temperature anomaly', 'number of spots', 'Volcanic Emmision',
            'CO2 W m2', 'CH4 W m2', 'N2O W m2']].corr(), annot=True, center = 0, cmap="crest")
        st.pyplot(viz.figure)

def result():
    st.markdown("<h1 style='text-align: center; color: grey;'>Health impact of climate change</h1>", unsafe_allow_html=True)

    with st.container():
                st.write('Extreme weather events are defined as anomalies denoting a significant departure from long-period average weather observations such as atmospheric temperature, wind speed, and precipitation. Droughts, periods of extreme heat or cold, and floods are examples of extreme weather events, and with accelerating climate change, the frequency and magnitude of these events are likely to increase')
                st.markdown("<h6 style='text-align: right; color: grey;'>Source EM-DAT: The OFDACRED International Disaster Database</h6>", unsafe_allow_html=True)

                fig = px.bar(df_disaster_reported, x = 'year', y = 'Number of disasters reported', title = 'Natural disasters reported 1900–2011' )
                st.plotly_chart(fig)
                
                st.write('Extreme heat and cold cause immediate rises in weather-related mortality. Natural hazards have been secondarily associated with infectious diseases, including diarrheal diseases, acute respiratory infections, malaria, leptospirosis, measles, dengue fever, viral hepatitis, typhoid fever, meningitis, tetanus and cutaneous mucormycosis')
                st.image('https://ars.els-cdn.com/content/image/1-s2.0-S2667278223000913-gr4.jpg')

    with st.container():
         st.write('Among infectious diseases, vector-borne (e.g.: mosquito-borne) diseases, including malaria, are among those most sensitive to a changing climate. For example, “globally, temperature increases of 2-3ºC would increase the number of people who, in climatic terms, are at risk of malaria by around 35%, i.e., by several hundred million, as the seasonal duration of malaria would increase in many currently endemic areas” ')
         st.markdown("<h6 style='text-align: center; color: black;'>Number of reported malaria cases in Djibouti, 2010–2020</h6>", unsafe_allow_html=True)
         st.markdown("<h6 style='text-align: right; color: grey;'>Source WHO</h6>", unsafe_allow_html=True)

         st.image('https://cdn.who.int/media/images/default-source/global-malaria-program-(gmp)/feature-stories/djibouti-an-stephensi.tmb-549v.png?sfvrsn=c3be647f_2')

    with st.container():
         option_mosq = st.selectbox(
            'Mosquito distribution',
            ('Today', 'In 2080, I DO care', "In 2080, I don't care"))
         if option_mosq=='Today':
            st.write('Current worldwide distribution of the mosquito')
            st.markdown("<h6 style='text-align: right; color: grey;'>Source https://sustainability.stanford.edu/</h6>", unsafe_allow_html=True)
            st.image('https://sustainability.stanford.edu/sites/sustainability/files/styles/card_1900x950/public/media/earth_news/disease-current-with-scale-final.png?h=185779e6&itok=NJ4C9cMS')
         elif option_mosq=='In 2080, I DO care':
            st.write('Predicted range of the mosquito in 2080 if the world exceeds Paris Agreement goals to reduce warming')
            st.markdown("<h6 style='text-align: right; color: grey;'>Source https://sustainability.stanford.edu/</h6>", unsafe_allow_html=True)

            st.image('https://sustainability.stanford.edu/sites/sustainability/files/styles/large/public/media/earth_news/aaa-disease-2080-exceed-final_0.png?itok=Z66q_dn9')
         elif option_mosq=="In 2080, I don't care":
            st.write('Predicted range of the mosquito in 2080 if there is no change to global greenhouse gas emissions')
            st.markdown("<h6 style='text-align: right; color: grey;'>Source https://sustainability.stanford.edu/</h6>", unsafe_allow_html=True)

            st.image('https://sustainability.stanford.edu/sites/sustainability/files/styles/large/public/media/earth_news/aaa-disease-2080-business-usual-final_0.png?itok=0t_smPb3')
            st.image('https://media.giphy.com/media/9JNkB9oRaAzJK/giphy.gif')



page_names_to_funcs = {
    "—": intro,
    "Proves": factors,
    "Factors": guilty,
    "Estimation of impact": impact,
    "Consequences" : result
}

demo_name = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()









