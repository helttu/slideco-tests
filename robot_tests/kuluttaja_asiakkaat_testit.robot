*** Settings ***
Library           Selenium2Library
Resource          ../robot_resources/common_resource.robot

*** Variables ***
${browser}        	    chrome
${selenium_speed}       0.25
${url_wd}   			http://finndeco.codemen.fi/build/?api=K3JK2FCG
${url_sms}   			http://finndeco.codemen.fi/manage/

*** Test Cases ***
Suunnitelman Tekeminen Ja Komerokoodin Tallennus
    [Tags]  kehitys
    Avaa Wardrobe Builder
    Klikkaa Aloita Suunnittelu Painiketta
    Valitse Korkeus
    Valitse Leveys Ja Klikkaa Seuraava Vaihe
    Valitse Liukuovien Määrä Ja Klikkaa Seuraava Vaihe
    Valitse Mieleisesi Liukuoviprofiili
    Valitse Mieleisesi Profiilisävy Ja Klikkaa Seuraava Vaihe
    Valitse Liukuoven Hidastimet Ja Klikkaa Seuraava Vaihe
    Valitse Mieleisesi Ovimalli Tästä Ja Klikkaa Seuraava Vaihe
    Lisää, Poista Tai Säädä Jakolistoja Mielesi Mukaan Ja Klikkaa Seuraava Vaihe
    Valitse Materiaalit Ja Klikkaa Seuraava Vaihe
    Valitse Runko-osat Ja Klikkaa Seuraava Vaihe
    Valitse Kehäsävy Ja Klikkaa Seuraava Vaihe
    Syötä Nimi, Asuinpaikkakunta Ja Sähköpostiosoite
    Tallenna Suunnitelma, Lähetä Ja Ota Komerokoodi Talteen
	[Teardown]    Close Browser

*** Keywords ***
Avaa Wardrobe Builder
    Open Browser                		${url_wd}    ${browser}
    Maximize Browser Window
    Set Selenium Speed          		${selenium_speed}
    Wait Until Element Is Visible  		//section[@id='section-welcome_message']/div[2]/button

Klikkaa Aloita Suunnittelu Painiketta
	Click Element    					//section[@id='section-welcome_message']/div[2]/button
	Wait Until Element Is Visible   	//section[@id='section-place_aperture']/div[5]/div[3]/div    timeout=30s

Valitse Korkeus
	Click Element    					//section[@id='section-place_aperture']/div[5]/div[3]/div    	# 2
	Wait Until Element Is Visible    	//section[@id='section-place_aperture']/div[5]/div[6]    timeout=30s
	Click Element    					//section[@id='section-place_aperture']/div[5]/div[6]    		# 5
	Wait Until Element Is Visible    	//section[@id='section-place_aperture']/div[2]/div/div

Valitse Leveys Ja Klikkaa Seuraava Vaihe
	Click Element    					//section[@id='section-place_aperture']/div[2]/div/div
	Wait Until Element Is Visible    	//section[@id='section-place_aperture']/div[5]/div[3]/div    timeout=30s
	Click Element    					//section[@id='section-place_aperture']/div[5]/div[3]/div
	Wait Until Element Is Visible    	//section[@id='section-progress_navigation']/div[5]    timeout=30s
	# Seuraaava vaihe
	Click Element    					//section[@id='section-progress_navigation']/div[5]
	Wait Until Element Is Visible    	//section[@id='section-sidebar_doors']/div[2]/div/div[2]/div[4]/div    timeout=30s

Valitse Liukuovien Määrä Ja Klikkaa Seuraava Vaihe
	# 2 kappeletta
	Click Element    					//section[@id='section-sidebar_doors']/div[2]/div/div[2]/div[4]
	Wait Until Element Is Visible    	//section[@id='section-progress_navigation']/div[5]/span    timeout=30
	Click Element    					//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible 		//section[@id='section-progress_navigation']/div[5]/span    timeout=30s

Valitse Mieleisesi Liukuoviprofiili
	# s200
	Click Element    					//section[@id='section-sidebar_profiles']/div[2]/div/div[2]/div[2]/div[2]
	Wait Until Element Is Visible   	//section[@id='section-progress_navigation']/div[5]/span    timeout=30s

Valitse Mieleisesi Profiilisävy Ja Klikkaa Seuraava Vaihe
	# Shampanja
	Click Element    					//section[@id='section-sidebar_profiles']/div[2]/div[2]/div[2]/div[2]/div[2]
	Wait Until Element Is Visible   	//section[@id='section-progress_navigation']/div[5]/span    timeout=30s
	# Seuraava vaihe
	Click Element     					//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible   	//section[@id='section-progress_navigation']/div[5]/span    timeout=30s

Valitse Liukuoven Hidastimet Ja Klikkaa Seuraava Vaihe
	Click Element 						//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible   	//section[@id='section-progress_navigation']/div[5]/span    timeout=30s
	# Seuraava vaihe
	Click Element    					//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible   	//section[@id='section-progress_navigation']/div[5]/span    timeout=30s

Valitse Runko-osat Ja Klikkaa Seuraava Vaihe
	Click Element 						//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible       //section[@id='section-progress_navigation']/div[5]/span    timeout=30s

Valitse Kehäsävy Ja Klikkaa Seuraava Vaihe
	# Pähkinä
	Click Element    					//section[@id='section-sidebar_frame']/div[2]/div[3]/div[2]/div[2]/div[2]
	Wait Until Element Is Visible   	//section[@id='section-progress_navigation']/div[5]/span    timeout=30s
	# Seuraava vaihe
	Click Element  						//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible  		//section[@id='section-progress_navigation']/div[5]/span

Valitse Mieleisesi Ovimalli Tästä Ja Klikkaa Seuraava Vaihe
	# Ylin, yksi
	Click Element   					//*[@id='section-sidebar_separators']/div[2]/div[1]/div[2]/div[1]/div/div
	Wait Until Element Is Visible  		//section[@id='section-progress_navigation']/div[5]/span    timeout=30s
	# Seuraava vaihe
	Click Element    					//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible  		//section[@id='section-progress_navigation']/div[5]/span    timeout=30s

Lisää, Poista Tai Säädä Jakolistoja Mielesi Mukaan Ja Klikkaa Seuraava Vaihe
	# Seuraava vaihe
	Click Element    					//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible     	//section[@id='section-progress_navigation']/div[5]/span    timeout=30s

Valitse Materiaalit Ja Klikkaa Seuraava Vaihe
	# Peilit
	Click Element    					//section[@id='section-sidebar_materials']/div[2]/div/div[2]/div[2]/div[3]
	Wait Until Element Is Visible    	css=img[alt="panelmaterial_finland_kirkas_peili"]    timeout=30s
	# Kirkas peili
	Click Element     					css=img[alt="panelmaterial_finland_kirkas_peili"]
	Wait Until Element Is Visible  		//section[@id='section-progress_navigation']/div[5]/span
	# Seuraava vaihe
	Click Element  						//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible  		//*[@id='furniture-prompt']/div[2]/button    timeout=30s
	# huom! popup
	Click Element   					//*[@id='furniture-prompt']/div[2]/button
	Wait Until Element Is Visible  		//section[@id='section-progress_navigation']/div[5]/span    timeout=30s
	Click Element    					//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible  		//section[@id='section-progress_navigation']/div[5]/span    timeout=30s

Valitse Runkosävy
	# Harmaa
	Click Element  						//*[@id='section-sidebar_furniture']/div[2]/div[2]/div[2]/div[3]/div[1]
	Wait Until Element Is Visible  		//section[@id='section-progress_navigation']/div[5]/span    timeout=30s
	Click Element    					//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible 		//section[@id='section-progress_navigation']/div[5]/span    timeout=30s

Mihin Käytät Vaatekaappiasi Kysymys 1/2
	# Eteinen
	Click Element  						//section[@id='section-sidebar_questionaire']/div/div/div/div[2]/div[3]/div/div/div[2]
	Wait Until Element Is Visible  		//section[@id='section-progress_navigation']/div[5]/span    timeout=30s
	Click Element    					//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible  		//section[@id='section-progress_navigation']/div[5]/span    timeout=30s

Kenen Makuuhuone Kysymys 2/2
	# Perhe
	Click Element   					//div[4]/div/div/div
	Wait Until Element Is Visible  		//section[@id='section-progress_navigation']/div[5]/span    timeout=30s
	Click Element    					//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible  		//div[@id='q-refine']/div[2]/div[2]/div[4]/div    timeout=30s

Valitse Mieleisesi Malli Suunnitelmasi Pohjaksi
	# Mekot ja puvut
	Click Element  						//*[@id='q-refine']/div[2]/div[2]/div[4]/div[1]
	Wait Until Element Is Visible  		//section[@id='section-progress_navigation']/div[5]/span    timeout=30s
	Click Element    					//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible    	//section[@id='section-progress_navigation']/div[5]/span    timeout=30s

Klikkaa Seurava Vaihe Huoneen Kuva Sivulla
	Click Element  						//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible  		//*[@id='section-sidebar_storage']/div/div[4]/form/button    								timeout=30s

Syötä Nimi, Asuinpaikkakunta Ja Sähköpostiosoite
	Click Element   					//*[@id='section-sidebar_storage']/div/div[4]/form/button
	# Nimi ja asuinpaikka
	Input Text  						name=full_name    				Testiautomaatio Helsinki
	Wait Until Element Is Visible   	name=email    					timeout=30s
	# Sähköposti
	Input Text  						name=email    					sami.stedt@q-factory.fi
	Wait Until Element Is Visible   	//*[@id='section-sidebar_storage']/div/div[4]/form/button    	timeout=30s

Tallenna Suunnitelma, Lähetä Ja Ota Komerokoodi Talteen
	Click Element   					//*[@id='section-sidebar_storage']/div/div[4]/form/button
	Wait Until Element Is Visible   	//*[@id='section-sidebar_storage']/div/div[4]/form/div[2]/span[1]    timeout=30s
	${koodi_1}=   						Get Text    //*[@id='section-sidebar_storage']/div/div[4]/form/div[2]/span[1]
	Set Global Variable    				${koodi_1}
	${koodi_2}=  						Get Text    //*[@id='section-sidebar_storage']/div/div[4]/form/div[2]/span[2]
	Set Global Variable    				${koodi_2}
	${koodi_3}=							Get Text    //*[@id='section-sidebar_storage']/div/div[4]/form/div[2]/span[3]
	Set Global Variable    				${koodi_3}
	${koodi_4}=  						Get Text    //*[@id='section-sidebar_storage']/div/div[4]/form/div[2]/span[4]
	Set Global Variable    				${koodi_4}
