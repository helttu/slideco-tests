*** Settings ***
Library           Selenium2Library

*** Variables ***
${browser}        	    chrome
${selenium_speed}       0.25
${url_wd}   			http://finndeco.codemen.fi/build/?api=K3JK2FCG
${url_sms}   			http://finndeco.codemen.fi/manage/

*** Keywords ***
Sisäänkirjaudu Slideco Management System
    [Arguments]     					${user}    					${pwd}
    Open Browser                        ${url_sms}    				${browser}
    Maximize Browser Window
    Set Selenium Speed                  ${selenium_speed}
    Input Text      					name=login          		${user}
    Input Text      					name=password       		${pwd}
    Click Element                       //*[@id='login-panel']/form/button
    Wait Until Element Is Visible       link=Track orders    		timeout=30s

Klikkaa Track Orders
	Click Element  						link=Track orders
	Wait Until Element Is Visible       //div[3]/div/input    timeout=30s

Klikkaa REG Kodin Terra Jyväskylä Dashboard
	Click Element  						link=REG Kodin Terra Jyväskylä Dashboard
	Wait Until Element Is Visible  		link=List Orders »    timeout=30s

Klikkaa See Variations
	Click Element 						link=See Variations »
	Wait Until Page Contains  			Door profiles    timeout=30s
	Wait Until Page Contains  			Material    timeout=30s
	Wait Until Page Contains  			Outer wooden frames    timeout=30s
	Wait Until Page Contains  			Interiors    timeout=30s
	Wait Until Page Contains  			Horizontal Bars    timeout=30s
	Wait Until Page Contains  			Soft Close    timeout=30s
	Wait Until Page Contains  			Extras    timeout=30s

Syötä Customer Name Ja Tarkista Tulokset
	[Arguments]     					${cust_name_input}    	${cust_name_result}    ${total}
	Input Text   						//div[3]/div/input    	${cust_name_input}
	Wait Until Element Is Visible  		//div[4]/select         timeout=30s
	# Creator
	Select From List   					//div[4]/select    		Customer
	Wait Until Page Contains   			${cust_name_result}     timeout=30s
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

Klikkaa Retailers
	Click Element   					link=Retailers
	Wait Until Element Is Visible   	//td[2]/button    timeout=30s

Klikkaa My Account
	Click Element  						link=My Account »
	Wait Until Element Is Visible  		//a[contains(text(),'REG Kodin Terra Jyväskylä')]    timeout=30s

Klikkaa Managers
	Click Element  						link=Managers
	Wait Until Element Is Visible  		//td[2]/button    timeout=30s

Klikkaa Set Prices
	Click Element  						link=Set prices
	Wait Until Element Is Visible   	//div[@id='retailer-content-floated']/div/div/div/div[2]/div/div/input    timeout=30s

Klikkaa Configure Applications
	Click Element   					link=Configure applications
	Wait Until Element Is Visible   	//td[2]/button
	Wait Until Page Contains  			REG Jyväskylä    timeout=30s

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
	Click Element  						//*[text()[contains(.,'OK')]]
	Sleep   							2s
	Wait Until Element Is Visible   	//*[text()[contains(.,'OK')]]    timeout=30s
	Click Element 						//*[text()[contains(.,'OK')]]
	Wait Until Page Contains  			${email}    timeout=30s

Poista Manager
	[Arguments]     					${email}
	Click Element  						//tr[30]/td[7]/button
	Wait Until Page Contains   			You are about to remove from retailer (no name)    timeout=30s
	Click Element 						//*[text()[contains(.,'OK')]]
	Wait Until Page Contains 			${email}    timeout=30s
	Reload Page
	Wait Until Page Does Not Contain    ${email}    timeout=30s

Syötä Merkkijono VAT Multiplier Kenttään
	[Arguments]     					${string}
	Input Text   						//div[@id='retailer-content-floated']/div/div/div/div[2]/div/div/input    ${string}
	Press Key               			//div[@id='retailer-content-floated']/div/div/div/div[2]/div/div/input    \\09

Tarkista Että Merkkijonoa Ei Hyväksytä
	Page Should Not Contain  			Retailer updated

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



