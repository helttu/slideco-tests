*** Settings ***
Library           Selenium2Library

*** Variables ***
${browser}        	    chrome
${selenium_speed}       0.25
${url_wd}   			http://finndeco.codemen.fi/build/?api=K3JK2FCG
${url_sms}   			http://finndeco.codemen.fi/manage/

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
	Click Element    					//section[@id='section-sidebar_doors']/div[2]/div/div[2]/div[4]/div
	Wait Until Element Is Visible    	//section[@id='section-progress_navigation']/div[5]/span    timeout=30
	Click Element    					//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible 		//section[@id='section-sidebar_profiles']/div[2]/div/div[2]/div[2]/div[2]    timeout=30s

Valitse Mieleisesi Liukuoviprofiili
	# s100
	Click Element    					//section[@id='section-sidebar_profiles']/div[2]/div/div[2]/div[2]/div[2]
	Wait Until Element Is Visible   	//section[@id='section-sidebar_profiles']/div[2]/div[2]/div[2]/div[2]/div[2]    timeout=30s

Valitse Mieleisesi Profiilisävy Ja Klikkaa Seuraava Vaihe
	# Tammi
	Click Element    					//section[@id='section-sidebar_profiles']/div[2]/div[2]/div[2]/div[2]/div[2]
	Wait Until Element Is Visible   	//section[@id='section-progress_navigation']/div[5]/span    timeout=30s
	# Seuraava vaihe
	Click Element     					//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible   	//section[@id='section-progress_navigation']/div[5]/span    timeout=30s

Valitse Liukuoven Hidastimet Ja Klikkaa Seuraava Vaihe
	Wait Until Page Contains 			Tähän profiiliin ei saa hidastinta    timeout=30s
	Wait Until Element Is Visible   	//section[@id='section-progress_navigation']/div[5]/span    timeout=30s
	# Seuraava vaihe
	Click Element    					//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible   	//*[@id='section-sidebar_frame']/div[2]/div[1]/div[2]/div/div[1]/label/label    timeout=30s

Valitse Runko-osat Ja Klikkaa Seuraava Vaihe
	# Kattolevy
	Click Element    					//*[@id='section-sidebar_frame']/div[2]/div[1]/div[2]/div/div[1]/label/label
	Wait Until Element Is Visible   	//section[@id='section-progress_navigation']/div[5]/span    timeout=30s
	Click Element 						//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible       //section[@id='section-sidebar_frame']/div[2]/div[3]/div[2]/div[2]/div[2]    timeout=30s

Valitse Kehäsävy Ja Klikkaa Seuraava Vaihe
	# Pähkinä
	Click Element    					//section[@id='section-sidebar_frame']/div[2]/div[3]/div[2]/div[2]/div[2]
	Wait Until Element Is Visible   	//section[@id='section-progress_navigation']/div[5]/span    timeout=30s
	# Seuraava vaihe
	Click Element  						//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible  		//section[@id='section-sidebar_separators']/div[2]/div/div[2]/div/div/div

Valitse Mieleisesi Ovimalli Tästä Ja Klikkaa Seuraava Vaihe
	# Ylin, yksi
	Click Element   					//section[@id='section-sidebar_separators']/div[2]/div/div[2]/div/div/div
	Wait Until Element Is Visible  		//section[@id='section-progress_navigation']/div[5]/span    timeout=30s
	# Seuraava vaihe
	Click Element    					//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible  		//section[@id='section-progress_navigation']/div[5]/span    timeout=30s

Lisää, Poista Tai Säädä Jakolistoja Mielesi Mukaan Ja Klikkaa Seuraava Vaihe
	# Seuraava vaihe
	Click Element    					//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible     	//section[@id='section-sidebar_materials']/div[2]/div/div[2]/div[2]/div[3]    timeout=30s

Valitse Materiaalit Ja Klikkaa Seuraava Vaihe
	Click Element    //section[@id='section-sidebar_materials']/div[2]/div/div[2]/div[2]/div[3]
	Wait Until Element Is Visible    	css=img[alt="panelmaterial_finland_kirkas_peili"]    timeout=30s
	Click Element     					css=img[alt="panelmaterial_finland_kirkas_peili"]
	Wait Until Element Is Visible  		//section[@id='section-progress_navigation']/div[5]/span    timeout=30s
	Click Element    					//section[@id='section-progress_navigation']/div[5]/span
	Wait Until Element Is Visible    	css=button[type="submit"]    timeout=30s

Tallenna Suunnitelma Ja Lähetä
	Click Element    					css=button[type="submit"]
	Wait Until Element Is Visible   	name=full_name    				timeout=30s
	Input Text  						name=full_name    				Testiautomaatio
	Wait Until Element Is Visible   	name=email    					timeout=30s
	Input Text  						name=email    					sami.stedt@q-factory.fi
	Wait Until Element Is Visible   	css=button[type="submit"]    	timeout=30s
	Click Element   					css=button[type="submit"]
	Wait Until Element Is Visible   	css=button[type="submit"]    	timeout=30s
	Click Element   					css=button[type="submit"]
	# Jaa tämä sivu, email
	Wait Until Element Is Visible  		//*[@id='section-sidebar_storage']/div/div[7]/div/div[2]/button[1]    timeout=30s

<<<<<<< HEAD
=======
# Tästä alkaa Slideco Management System keywordit

>>>>>>> 238cb814bff28a062433d8118c4d0b07aaba26b6
Sisäänkirjaudu Slideco Management System
    [Arguments]     					${user}    ${pwd}
    Open Browser                        ${url_sms}    ${browser}
    Maximize Browser Window
    Set Selenium Speed                  ${selenium_speed}
    Input Text      					name=login          ${user}
    Input Text      					name=password       ${pwd}
    Click Element                       css=button.btn.btn-default
    Wait Until Element Is Visible       link=Track orders    timeout=30s

Klikkaa Track Orders
	Click Element  						link=Track orders
	Wait Until Element Is Visible       //div[3]/div/input    timeout=30s

<<<<<<< HEAD
Syötä Customer Name Ja Tarkista Tulokset
	[Arguments]     					${ref_cust_name}    ${total}
	Input Text   						//div[3]/div/input    	${ref_cust_name}
	Wait Until Element Is Visible  		//div[4]/select         timeout=30s
	# Creator
	Select From List   					//div[4]/select    		Customer
	Wait Until Page Contains   			${total}   				timeout=30s

Valitse Creator Ja Tarkista Tulokset
	[Arguments]     						${creator}    ${customer}
	Select From List   			    	//div[4]/select    	${creator}
	Wait Until Page Contains  			${customer}    timeout=30s

Klikkaa Descending Ja Tarkista Pvm
	[Arguments]     					${created_desc}
	Click Element   					//button[2]
	Wait Until Page Contains    		${created_desc}

Klikkaa Ascending Ja Tarkista Pvm
	[Arguments]     					${created_asc}
	Click Element   					//span/button
	Wait Until Page Contains    		${created_asc}

=======
Klikkaa Retailers
	Click Element   					link=Retailers
	Wait Until Element Is Visible   	//td[2]/button    timeout=30s

Klikkaa Managers
	Click Element  						link=Managers
	Wait Until Element Is Visible  		//td[2]/button    timeout=30s

Klikkaa Set Prices
	Click Element  						link=Set prices
	Wait Until Element Is Visible   	//div[@id='retailer-content-floated']/div/div/div/div[2]/div/div/input    timeout=30s

Klikkaa Configure Applications
	Click Element   					link=Configure applications
	Wait Until Element Is Visible   	//td[2]/button

Syötä Customer Name Ja Tarkista
	[Arguments]     					${customer_name}    ${total}
	Input Text   						//div[3]/div/input    	${customer_name}
	Wait Until Page Contains   			${customer_name}    		timeout=30s
	Wait Until Page Contains   			${total}    			timeout=30s

Valitse Creator Ja Tarkista
	[Arguments]     					${creator}    ${customer_name}    ${total}
	Select From List   					//div[4]/select    ${creator}
	Wait Until Page Contains   			${customer_name}    		timeout=30s
	Wait Until Page Contains   			${total}    			timeout=30s

Valitse Descending Ja Tarkista
	[Arguments]     					${created}
	Click Element   					//button[2]
	Wait Until Page Contains  			${created}    timeout=30s

Valitse Ascending Ja Tarkista
	[Arguments]     					${created}
	Click Element   					//span/button
	Wait Until Page Contains  			${created}    timeout=30s

Tarkista Retailersien Listaus
	[Arguments]     					${ret1}    ${ret2}    ${ret3}    ${ret4}    ${ret5}
	Wait Until Page Contains  			${ret1}        timeout=30s
	Wait Until Page Contains  			${ret2}        timeout=30s
	Wait Until Page Contains  			${ret3}        timeout=30s
	Wait Until Page Contains  			${ret4}       	timeout=30s
	Wait Until Page Contains  			${ret5}    		timeout=30s

Klikkaa Edit ja Tarkista Tiedot
	[Arguments]     					${title}
	Click Element   					xpath=(//a[contains(@href, '#/dash/retailers/24/edit')])[2]
	Wait Until Page Contains   			${title}    timeout=30s

Klikkaa Invite Ja Syötä Retailer Email
	[Arguments]     					${email}
	Click Element   					//td[2]/button
	Wait Until Element Is Visible  		//input[@type='text']    timeout=30s
	Input Text  						//input[@type='text']    ${email}
	Click Element  						xpath=(//button[@type='button'])[3]
	Sleep  								2s
	Wait Until Element Is Visible  		xpath=(//button[@type='button'])[2]   timeout=30s
	Click Element   					xpath=(//button[@type='button'])[2]
	Sleep   							2s
	Wait Until Page Contains  			${email}    timeout=30s

Poista Manager
	[Arguments]     					${email}
	Click Element  						//*[@id='retailer-content-floated']/div/div/div/div[2]/table/tbody/tr[23]/td[7]/button
	Sleep  								2s
	Wait Until Page Contains   			You are about to remove from retailer (no name)    timeout=30s
	Click Element 						xpath=(//button[@type='button'])[3]
	Wait Until Page Contains 			${email}    timeout=30s
	Reload Page
	Wait Until Page Does Not Contain    ${email}    timeout=30s

Syötä Merkkijono VAT Multiplier Kenttään
	[Arguments]     					${string}
	Input Text   						//div[@id='retailer-content-floated']/div/div/div/div[2]/div/div/input    ${string}

Tarkista Että Merkkijonoa Ei Hyväksytä
	Wait Until Page Does Not Contain   	Retailer updated    timeout=30s

Klikkaa Create New Application
	Click Element  						//td[2]/button
	Wait Until Element Is Visible   	//div[2]/input    timeout=30s

Syötä Location
	[Arguments]     					${location}
	Input Text   						//div[2]/input    ${location}

Syötä Title (Short Description)
	[Arguments]     					${title}
	Input Text   						//div[3]/input    ${title}

Klikkaa Link To Application Linkkiä
	Click Element  						link=Open in new window (tab)
	Wait Until Element Is Visible  		//*[@id='section-welcome_message']/div[2]/button    timeout=30s
	Switch Browser                      1

Valitse Display Price Breakdown in Web Application?
	[Arguments]     					${enabled}
	Select From List					//div[5]/select    ${enabled}

Valitse Display callback in Web Application?
	[Arguments]     					${enabled}
	Select From List   						//div[6]/select    ${enabled}

Valitse Enable Interiors
	[Arguments]     					${enabled}
	Select From List   						//div[7]/select    ${enabled}

Valitse Enable Questionaire
	[Arguments]     					${enabled}
	Select From List   						//div[8]/select    ${enabled}

Valitse Application Type
	[Arguments]     					${type}
	Select From List   						//div[9]/select    ${type}

Valitse Colour Scheme
	[Arguments]     					${colour}
	Select From List   						//div[10]/select    ${colour}

Valitse Language
	[Arguments]     					${language}
	Select From List   						//div[11]/select    ${language}

Syötä Share Message
	[Arguments]     					${message}
	Input Text   						//textarea    ${message}
>>>>>>> 238cb814bff28a062433d8118c4d0b07aaba26b6



