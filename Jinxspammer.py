--// SERVICES
local TweenService = game:GetService("TweenService")
local Lighting = game:GetService("Lighting")
local Players = game:GetService("Players")
local SoundService = game:GetService("SoundService")
local TextChatService = game:GetService("TextChatService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local UserInputService = game:GetService("UserInputService")

local plr = Players.LocalPlayer

--// EXECUTOR-SAFE INTERFACE LAYER
local pgui = nil
if gethui then
    pgui = gethui()
elseif syn and syn.protect_gui then
    local protectedScreen = Instance.new("ScreenGui")
    syn.protect_gui(protectedScreen)
    protectedScreen.Parent = game:GetService("CoreGui")
    pgui = protectedScreen
else
    pgui = plr:FindFirstChildOfClass("PlayerGui")
end

--// EXACT REMOTES FROM THE SOURCE SCRIPT
local RE = ReplicatedStorage:WaitForChild("RE", 5)
local NameRemote = RE and RE:WaitForChild("1RPNam1eTex1t", 5) or nil
local ColorRemote = RE and RE:WaitForChild("1RPNam1eColo1r", 5) or nil

--// FIXED PALETTES
local PureWhite = Color3.fromRGB(255, 255, 255)
local OffWhite = Color3.fromRGB(240, 245, 250)
local SoftBlue = Color3.fromRGB(200, 220, 245)
local DeepTextDark = Color3.fromRGB(20, 25, 35)
local MutedText = Color3.fromRGB(90, 105, 125)
local DarkBorder = Color3.fromRGB(180, 200, 225)
local GrayAccent = Color3.fromRGB(140, 160, 190)

local blur = Instance.new("BlurEffect", Lighting)
blur.Size = 0

--// DESTROY PRIOR RENDERS
if pgui:FindFirstChild("ᴊɪɴ x ᴊɪɴ_MATRIX") then
    pgui["ᴊɪɴ x ᴊɪɴ_MATRIX"]:Destroy()
end

local gui = Instance.new("ScreenGui")
gui.Name = "ᴊɪɴ x ᴊɪɴ_MATRIX"
gui.Parent = pgui
gui.IgnoreGuiInset = true
gui.ResetOnSpawn = false

--==================================================
-- CONTROLLABLE DYNAMIC NEON SNOWFLAKE SYSTEM
--==================================================
local snowFolder = Instance.new("Folder", gui)
snowFolder.Name = "SnowContainer"

local snowActive = false
local currentNeonColor = PureWhite

local function createSnowflake()
    if not snowActive then return end
    
    local flake = Instance.new("TextLabel")
    flake.Text = "❆"
    flake.Font = Enum.Font.GothamBold
    flake.TextColor3 = currentNeonColor
    flake.BackgroundTransparency = 1
    flake.TextSize = math.random(14, 24)
    flake.Size = UDim2.new(0, 30, 0, 30)
    flake.TextTransparency = math.random(1, 4) / 10
    
    local startX = math.random()
    flake.Position = UDim2.new(startX, 0, -0.05, 0)
    flake.Parent = snowFolder

    task.spawn(function()
        local fallSpeed = math.random(15, 35) / 1000
        local swayAmplitude = math.random(15, 40) / 1000
        local swaySpeed = math.random(2, 5)
        local currentY = -0.05
        local timeAlive = 0

        while flake and flake.Parent and currentY < 1.05 and snowActive do
            local dt = task.wait(0.03)
            timeAlive = timeAlive + dt
            currentY = currentY + fallSpeed
            local currentX = startX + math.sin(timeAlive * swaySpeed) * swayAmplitude
            flake.Position = UDim2.new(currentX, 0, currentY, 0)
            flake.TextColor3 = currentNeonColor
        end
        
        if flake and flake.Parent then
            if not snowActive then
                local tween = TweenService:Create(flake, TweenInfo.new(0.5, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), {TextTransparency = 1})
                tween:Play()
                tween.Completed:Wait()
            end
            flake:Destroy()
        end
    end)
end

local function setSnowEnabled(state)
    snowActive = state
    if snowActive then
        task.spawn(function()
            while snowActive and gui and gui.Parent do
                createSnowflake()
                task.wait(0.12)
            end
        end)
    else
        for _, flake in pairs(snowFolder:GetChildren()) do
            if flake:IsA("TextLabel") then
                TweenService:Create(flake, TweenInfo.new(0.5, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), {TextTransparency = 1}):Play()
                task.delay(0.5, function()
                    if flake then flake:Destroy() end
                end)
            end
        end
    end
end

--==================================================
-- UI ELEMENT 1: PROGRESS BOOT STRAPPER
--==================================================
local bootFrame = Instance.new("Frame", gui)
bootFrame.Size = UDim2.new(0, 440, 0, 260)
bootFrame.Position = UDim2.new(0.5, -220, 0.5, -130)
bootFrame.BackgroundColor3 = PureWhite
Instance.new("UICorner", bootFrame).CornerRadius = UDim.new(0, 14)

local bootGrad = Instance.new("UIGradient", bootFrame)
bootGrad.Color = ColorSequence.new({
    ColorSequenceKeypoint.new(0, PureWhite),
    ColorSequenceKeypoint.new(0.6, Color3.fromRGB(235, 243, 252)),
    ColorSequenceKeypoint.new(1, Color3.fromRGB(180, 210, 245))
})
bootGrad.Rotation = 45

local bootStrk = Instance.new("UIStroke", bootFrame)
bootStrk.Thickness = 2
bootStrk.Color = GrayAccent

local bootTitle = Instance.new("TextLabel", bootFrame)
bootTitle.Size = UDim2.new(1, 0, 0, 40)
bootTitle.Position = UDim2.new(0, 0, 0, 30)
bootTitle.Text = "ᴊɪɴ X ᴊɪɴ SPAMMER"
bootTitle.Font = Enum.Font.GothamBlack
bootTitle.TextColor3 = DeepTextDark
bootTitle.TextSize = 22
bootTitle.BackgroundTransparency = 1

local barBg = Instance.new("Frame", bootFrame)
barBg.Size = UDim2.new(0.8, 0, 0, 6)
barBg.Position = UDim2.new(0.1, 0, 0, 130)
barBg.BackgroundColor3 = DarkBorder
Instance.new("UICorner", barBg).CornerRadius = UDim.new(0, 3)

local barFill = Instance.new("Frame", barBg)
barFill.Size = UDim2.new(0, 0, 1, 0)
barFill.BackgroundColor3 = Color3.fromRGB(50, 140, 240)
Instance.new("UICorner", barFill).CornerRadius = UDim.new(0, 3)

local bootStatus = Instance.new("TextLabel", bootFrame)
bootStatus.Size = UDim2.new(1, 0, 0, 20)
bootStatus.Position = UDim2.new(0, 0, 0, 150)
bootStatus.Text = "Status: Authenticating Matrix Arrays..."
bootStatus.Font = Enum.Font.Code
bootStatus.TextColor3 = MutedText
bootStatus.TextSize = 11
bootStatus.BackgroundTransparency = 1

--==================================================
-- SAFE FADE UTILITY FUNCTIONS
--==================================================
local function fadeInFrame(targetFrame)
    targetFrame.Visible = true
    TweenService:Create(targetFrame, TweenInfo.new(0.4, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), {BackgroundTransparency = 0}):Play()

    for _, child in pairs(targetFrame:GetDescendants()) do
        if child:IsA("UIStroke") then
            TweenService:Create(child, TweenInfo.new(0.4, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), {Transparency = 0}):Play()
        elseif child:IsA("TextLabel") then
            TweenService:Create(child, TweenInfo.new(0.4, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), {TextTransparency = 0}):Play()
        elseif child:IsA("TextBox") or child:IsA("TextButton") then
            TweenService:Create(child, TweenInfo.new(0.4, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), {BackgroundTransparency = 0, TextTransparency = 0}):Play()
        elseif child:IsA("ImageLabel") then
            TweenService:Create(child, TweenInfo.new(0.4, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), {BackgroundTransparency = 0, ImageTransparency = 0}):Play()
        end
    end
end

local function fadeOutFrame(targetFrame)
    TweenService:Create(targetFrame, TweenInfo.new(0.35, Enum.EasingStyle.Quad, Enum.EasingDirection.In), {BackgroundTransparency = 1}):Play()

    for _, child in pairs(targetFrame:GetDescendants()) do
        if child:IsA("UIStroke") then
            TweenService:Create(child, TweenInfo.new(0.35, Enum.EasingStyle.Quad, Enum.EasingDirection.In), {Transparency = 1}):Play()
        elseif child:IsA("TextLabel") then
            TweenService:Create(child, TweenInfo.new(0.35, Enum.EasingStyle.Quad, Enum.EasingDirection.In), {TextTransparency = 1}):Play()
        elseif child:IsA("TextBox") or child:IsA("TextButton") then
            TweenService:Create(child, TweenInfo.new(0.35, Enum.EasingStyle.Quad, Enum.EasingDirection.In), {BackgroundTransparency = 1, TextTransparency = 1}):Play()
        elseif child:IsA("ImageLabel") then
            TweenService:Create(child, TweenInfo.new(0.35, Enum.EasingStyle.Quad, Enum.EasingDirection.In), {BackgroundTransparency = 1, ImageTransparency = 1}):Play()
        end
    end
end

--==================================================
-- UI ELEMENT 2: WELCOME SCREEN MODULE
--==================================================
local welcomeUI = Instance.new("Frame", gui)
welcomeUI.Size = UDim2.new(0, 340, 0, 340)
welcomeUI.Position = UDim2.new(0.5, -170, 0.5, -170)
welcomeUI.BackgroundColor3 = PureWhite
welcomeUI.BackgroundTransparency = 1
welcomeUI.Visible = false
Instance.new("UICorner", welcomeUI).CornerRadius = UDim.new(0, 18)

local welcGrad = Instance.new("UIGradient", welcomeUI)
welcGrad.Color = ColorSequence.new({
    ColorSequenceKeypoint.new(0, PureWhite),
    ColorSequenceKeypoint.new(0.65, Color3.fromRGB(235, 243, 252)),
    ColorSequenceKeypoint.new(1, Color3.fromRGB(180, 210, 245))
})
welcGrad.Rotation = 45

local welcStrk = Instance.new("UIStroke", welcomeUI)
welcStrk.Thickness = 2.5
welcStrk.Transparency = 1
welcStrk.Color = GrayAccent

local avatar = Instance.new("ImageLabel", welcomeUI)
avatar.Size = UDim2.new(0, 56, 0, 56)
avatar.Position = UDim2.new(0, 25, 0, 25)
avatar.BackgroundColor3 = Color3.fromRGB(240, 245, 250)
avatar.BackgroundTransparency = 1
avatar.ImageTransparency = 1
avatar.BorderSizePixel = 0
Instance.new("UICorner", avatar).CornerRadius = UDim.new(0, 12)

pcall(function()
    avatar.Image = Players:GetUserThumbnailAsync(plr.UserId, Enum.ThumbnailType.HeadShot, Enum.ThumbnailSize.Size150x150)
end)

local greetName = Instance.new("TextLabel", welcomeUI)
greetName.Size = UDim2.new(0, 220, 0, 56)
greetName.Position = UDim2.new(0, 93, 0, 25)
greetName.Text = "Welcome,\n" .. plr.DisplayName
greetName.Font = Enum.Font.GothamBold
greetName.TextColor3 = DeepTextDark
greetName.TextSize = 16
greetName.TextTransparency = 1
greetName.TextXAlignment = Enum.TextXAlignment.Left
greetName.BackgroundTransparency = 1

local desc1 = Instance.new("TextLabel", welcomeUI)
desc1.Size = UDim2.new(1, -50, 0, 25)
desc1.Position = UDim2.new(0, 25, 0, 110)
desc1.Text = "The best spammer with combo version"
desc1.Font = Enum.Font.GothamMedium
desc1.TextColor3 = Color3.fromRGB(220, 40, 40)
desc1.TextSize = 14
desc1.TextTransparency = 1
desc1.TextXAlignment = Enum.TextXAlignment.Left
desc1.BackgroundTransparency = 1

local desc2 = Instance.new("TextLabel", welcomeUI)
desc2.Size = UDim2.new(1, -50, 0, 20)
desc2.Position = UDim2.new(0, 25, 0, 135)
desc2.Text = "Made by ᴊɪɴ"
desc2.Font = Enum.Font.Code
desc2.TextColor3 = MutedText
desc2.TextSize = 12
desc2.TextTransparency = 1
desc2.TextXAlignment = Enum.TextXAlignment.Left
desc2.BackgroundTransparency = 1

local desc3 = Instance.new("TextLabel", welcomeUI)
desc3.Size = UDim2.new(1, -50, 0, 20)
desc3.Position = UDim2.new(0, 25, 0, 160)
desc3.Text = "H8 diya to cudega 🌶️💀!"
desc3.Font = Enum.Font.GothamBold
desc3.TextColor3 = DeepTextDark
desc3.TextSize = 12
desc3.TextTransparency = 1
desc3.TextXAlignment = Enum.TextXAlignment.Left
desc3.BackgroundTransparency = 1

local startBtn = Instance.new("TextButton", welcomeUI)
startBtn.Size = UDim2.new(1, -50, 0, 50)
startBtn.Position = UDim2.new(0, 25, 0, 250)
startBtn.Text = "ENGAGE TRANSMISSION MATRIX"
startBtn.BackgroundColor3 = Color3.fromRGB(50, 140, 240)
startBtn.BackgroundTransparency = 1
startBtn.TextColor3 = PureWhite
startBtn.TextTransparency = 1
startBtn.Font = Enum.Font.GothamBlack
startBtn.TextSize = 13
Instance.new("UICorner", startBtn).CornerRadius = UDim.new(0, 10)

local btnStrk = Instance.new("UIStroke", startBtn)
btnStrk.Thickness = 1.5
btnStrk.Transparency = 1
btnStrk.Color = GrayAccent

--==================================================
-- UI ELEMENT 3: DASHBOARD
--==================================================
local main = Instance.new("Frame", gui)
main.Visible = false
main.Size = UDim2.new(0, 560, 0, 340)
main.Position = UDim2.new(0.5, -280, 1, 50)
main.BackgroundColor3 = PureWhite
Instance.new("UICorner", main).CornerRadius = UDim.new(0, 16)

local mainGrad = Instance.new("UIGradient", main)
mainGrad.Color = ColorSequence.new({
    ColorSequenceKeypoint.new(0, PureWhite),
    ColorSequenceKeypoint.new(0.5, Color3.fromRGB(240, 246, 255)),
    ColorSequenceKeypoint.new(0.85, Color3.fromRGB(205, 226, 250)),
    ColorSequenceKeypoint.new(1, Color3.fromRGB(165, 200, 242))
})
mainGrad.Rotation = 45

local mainStrk = Instance.new("UIStroke", main)
mainStrk.Thickness = 2
mainStrk.Color = GrayAccent

local mainHeader = Instance.new("TextLabel", main)
mainHeader.Size = UDim2.new(1, -90, 0, 40)
mainHeader.Position = UDim2.new(0, 20, 0, 12)
mainHeader.Text = "⚡ ᴊɪɴ・一仁じん二二二二二二フ // SYSTEM CORE"
mainHeader.Font = Enum.Font.GothamBlack
mainHeader.TextColor3 = DeepTextDark
mainHeader.TextSize = 17
mainHeader.TextXAlignment = Enum.TextXAlignment.Left
mainHeader.BackgroundTransparency = 1

local closeBtn = Instance.new("TextButton", main)
closeBtn.Size = UDim2.new(0, 32, 0, 32)
closeBtn.Position = UDim2.new(1, -42, 0, 12)
closeBtn.Text = "X"
closeBtn.Font = Enum.Font.GothamBold
closeBtn.TextColor3 = PureWhite
closeBtn.TextSize = 16
closeBtn.BackgroundColor3 = Color3.fromRGB(220, 50, 50)
closeBtn.ZIndex = 10
Instance.new("UICorner", closeBtn).CornerRadius = UDim.new(0, 8)

local targetsContainer = Instance.new("Frame", main)
targetsContainer.Size = UDim2.new(0, 340, 0, 160)
targetsContainer.Position = UDim2.new(0, 20, 0, 65)
targetsContainer.BackgroundTransparency = 1

local gridLayout = Instance.new("UIGridLayout", targetsContainer)
gridLayout.CellSize = UDim2.new(0, 160, 0, 65)
gridLayout.CellPadding = UDim2.new(0, 15, 0, 15)

local names = {}
for i = 1, 4 do
    local containerFrame = Instance.new("Frame", targetsContainer)
    containerFrame.BackgroundColor3 = Color3.fromRGB(245, 248, 253)
    Instance.new("UICorner", containerFrame).CornerRadius = UDim.new(0, 8)

    local cStrk = Instance.new("UIStroke", containerFrame)
    cStrk.Thickness = 1
    cStrk.Color = DarkBorder

    local box = Instance.new("TextBox", containerFrame)
    box.Size = UDim2.new(1, -20, 1, 0)
    box.Position = UDim2.new(0, 10, 0, 0)
    box.PlaceholderText = "TARGET " .. i
    box.PlaceholderColor3 = GrayAccent
    box.BackgroundColor3 = Color3.fromRGB(245, 248, 253)
    box.BackgroundTransparency = 1
    box.TextColor3 = DeepTextDark
    box.Font = Enum.Font.GothamBold
    box.TextSize = 11
    box.BorderSizePixel = 0
    names[i] = box
end

local configContainer = Instance.new("Frame", main)
configContainer.Size = UDim2.new(0, 160, 0, 150)
configContainer.Position = UDim2.new(0, 380, 0, 65)
configContainer.BackgroundColor3 = Color3.fromRGB(245, 248, 253)
Instance.new("UICorner", configContainer).CornerRadius = UDim.new(0, 10)

local configStrk = Instance.new("UIStroke", configContainer)
configStrk.Thickness = 1
configStrk.Color = DarkBorder

local speedLabel = Instance.new("TextLabel", configContainer)
speedLabel.Size = UDim2.new(1, 0, 0, 25)
speedLabel.Position = UDim2.new(0, 0, 0, 15)
speedLabel.Text = "RUNTIME DELAY"
speedLabel.Font = Enum.Font.GothamBlack
speedLabel.TextColor3 = MutedText
speedLabel.TextSize = 10
speedLabel.BackgroundTransparency = 1

local speed = Instance.new("TextBox", configContainer)
speed.Size = UDim2.new(0.8, 0, 0, 45)
speed.Position = UDim2.new(0.1, 0, 0, 48)
speed.Text = "0.8"
speed.PlaceholderText = "0.8"
speed.BackgroundColor3 = PureWhite
speed.TextColor3 = DeepTextDark
speed.Font = Enum.Font.Code
speed.TextSize = 16
speed.BorderSizePixel = 0
Instance.new("UICorner", speed).CornerRadius = UDim.new(0, 6)

local speedStrk = Instance.new("UIStroke", speed)
speedStrk.Thickness = 1
speedStrk.Color = DarkBorder

local start = Instance.new("TextButton", main)
start.Size = UDim2.new(1, -40, 0, 55)
start.Position = UDim2.new(0, 20, 0, 250)
start.Text = "START ᴊɪɴ_ᴢᴇɴɪɴ ꜱᴘᴀ姆ᴍᴇR"
start.BackgroundColor3 = PureWhite
start.TextColor3 = DeepTextDark
start.Font = Enum.Font.GothamBlack
start.TextSize = 14
Instance.new("UICorner", start).CornerRadius = UDim.new(0, 10)

local startGrad = Instance.new("UIGradient", start)
startGrad.Rotation = 45

local startStrk = Instance.new("UIStroke", start)
startStrk.Thickness = 2
startStrk.Color = GrayAccent

--==================================================
-- TOGGLE & CLOSE SYSTEM CONTROLS
--==================================================
local panelOpen = false

local function setPanelState(open)
    panelOpen = open
    local targetMainPos = panelOpen and UDim2.new(0.5, -280, 0.5, -170) or UDim2.new(0.5, -280, 1, 50)
    TweenService:Create(main, TweenInfo.new(0.4, Enum.EasingStyle.Quint, Enum.EasingDirection.Out), {Position = targetMainPos}):Play()
    TweenService:Create(blur, TweenInfo.new(0.5), {Size = panelOpen and 24 or 0}):Play()
    
    setSnowEnabled(panelOpen)
end

closeBtn.MouseButton1Click:Connect(function()
    setPanelState(false)
end)

local toggle = Instance.new("TextButton", gui)
toggle.Visible = false
toggle.Size = UDim2.new(0, 120, 0, 40)
toggle.Position = UDim2.new(0, 20, 1, -55)
toggle.BackgroundColor3 = PureWhite
toggle.Text = "⚡ JIN MENU"
toggle.Font = Enum.Font.GothamBold
toggle.TextColor3 = DeepTextDark
toggle.TextSize = 12
toggle.ZIndex = 20
Instance.new("UICorner", toggle).CornerRadius = UDim.new(0, 10)

local toggleGrad = Instance.new("UIGradient", toggle)
toggleGrad.Rotation = 45

local toggleStrk = Instance.new("UIStroke", toggle)
toggleStrk.Thickness = 2
toggleStrk.Color = GrayAccent

toggle.MouseButton1Click:Connect(function()
    setPanelState(not panelOpen)
end)

--==================================================
-- WORD-SPAM LOGIC
--==================================================
local running = false
local word = {
    "TBX KUDAI Dining Table ✨",
    "Bed Sheet 💎",
    "TBX MEI Keyboard 🔥",
    "TBX KUDAI Notebook 🥀",
    "TBX MEI Running Shoes ⚖️",
    "TBX MARE Running Shoes ⚡",
    "TMX MARE Ceiling Fan 💫",
    "TBX MEI Desk Lamp ✨",
    "TBX KUDAI Ceiling Fan 🔮",
    "TBX KUDAI Ceiling Fan 🔥",
    "TBX MEI Bicycle 🥀",
    "TMX KUDAI Bed Sheet 🔮",
    "TBX KUDAI Wall Clock 💎",
    "TBX MARE Smart Phone 💥",
    "TMX MEI Headphones 💎",
    "TBX KUDAI Coffee Mug 🔮",
    "TMX KUDAI Desk Lamp 💧",
    "TBX MEI Running Shoes 💥",
    "TBX MEI Ceiling Fan 🥀",
    "TMX KUDAI Notebook 🔥",
    "Dining Table 💧",
    "TBX MARE Smart Phone 🔮",
    "TBX MEI Water Bottle 💫",
    "TMX MEI Umbrella 💥",
    "TMX MEI Wooden Door 💥",
    "TMX MARE Backpack 🔥",
    "TBX MARE Coffee Mug 🥀",
    "TBX MARE Desk Lamp 💥",
    "TMX MEI Bed Sheet 💧",
    "TBX KUDAI Bed Sheet 🥀",
    "TMX MARE Headphones 💥",
    "TMX MEI Toothbrush 🔥"
}

local function send(msg)
    local ch = TextChatService:FindFirstChild("TextChannels") and TextChatService.TextChannels:FindFirstChild("RBXGeneral")
    if ch then 
        pcall(function() ch:SendAsync(msg) end) 
    else
        local legacyChat = ReplicatedStorage:FindFirstChild("DefaultChatSystemChatEvents")
        if legacyChat and legacyChat:FindFirstChild("SayMessageRequest") then
            pcall(function() legacyChat.SayMessageRequest:FireServer(msg, "All") end)
        end
    end
end

start.MouseButton1Click:Connect(function()
    running = not running
    start.Text = running and "TERMINATE SYSTEM" or "START ・一仁じん二二二二二二フ ꜱᴘᴀ姆ᴍᴇR"
    
    if running then
        startGrad.Enabled = false
        start.BackgroundColor3 = Color3.fromRGB(220, 40, 40)
        start.TextColor3 = PureWhite
        startStrk.Color = Color3.fromRGB(255, 80, 80)
    else
        startGrad.Enabled = true
        start.BackgroundColor3 = PureWhite
        start.TextColor3 = DeepTextDark
    end

    if running then
        task.spawn(function()
            while running do
                local sp = tonumber(speed.Text) or 0.8
                for i, b in ipairs(names) do
                    if not running then break end
                    if b.Text ~= "" then
                        local targetDisplay = b.Text:upper()

                        -- Generate 7 random words safely
                        local w = {}
                        for idx = 1, 7 do
                            w[idx] = word[math.random(#word)] .. " "
                        end

                        local patterns = {
                            "@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@ [" .. targetDisplay .. "] " .. w[1] .. "[" .. targetDisplay .. "] " .. w[2] .. "[" .. targetDisplay .. "] " .. w[3] .. "\n@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@",
                            "[" .. targetDisplay .. "] " .. w[1] .. "[" .. targetDisplay .. "] " .. w[2] .. "[" .. targetDisplay .. "] " .. w[3] .. "\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-",
                            "|o_0||o_0||o_0||o_0||o_0||o_0||o_0||o_0||o_0||o_0||o_0||o_0||o_0||o_0||o_0||o_0||o_0|\n[" .. targetDisplay .. "] " .. w[1] .. "[" .. targetDisplay .. "] " .. w[2] .. "[" .. targetDisplay .. "] " .. w[3],
                            "[" .. targetDisplay .. "] " .. w[1] .. "[" .. targetDisplay .. "] " .. w[2] .. "[" .. targetDisplay .. "] " .. w[3] .. "\n(x)(x)(x)(x)(x)(x)(x)(x)(x)(x)(x)(x)(x)(x)(x)(x)(x)(x)(x)(x)(x)",
                            "---------------------------------------------------------------------------------\n[" .. targetDisplay .. "] " .. w[1] .. "[" .. targetDisplay .. "] " .. w[2] .. "[" .. targetDisplay .. "] " .. w[3],
                            "============================================================================================================\n[" .. targetDisplay .. "] " .. w[1] .. "[" .. targetDisplay .. "] " .. w[2] .. "[" .. targetDisplay .. "] " .. w[3]
                        }
                        
                        local selectedPattern = patterns[math.random(1, #patterns)]
                        send(selectedPattern)
                        task.wait(sp)
                    end
                end
                task.wait(0.1)
            end
        end)
    end
end)

--==================================================
-- IDENTITY AND RP COLORING
--==================================================
local function applyIdentity()
    if NameRemote then
        NameRemote:FireServer("RolePlayName","* JIN ﾒ ZENIN SPA姆MER *")
        NameRemote:FireServer("RolePlayBio","* ・一仁じん二二二二二二フ *")
    end
end

--==================================================
-- WHITE TO VIBRANT LIGHT BLUE SEQUENTIAL ENGINE
--==================================================
local function startWhiteNeon()
    task.spawn(function()
        while true do
            local t = (math.sin(tick() * 2) + 1) / 2
            local pureWhite = Color3.fromRGB(255, 255, 255)
            local lightBlue = Color3.fromRGB(50, 165, 255)
            local currentColor = pureWhite:Lerp(lightBlue, t)
            
            currentNeonColor = currentColor
            
            local dynamicSeq = ColorSequence.new({
                ColorSequenceKeypoint.new(0, pureWhite),
                ColorSequenceKeypoint.new(0.5, currentColor),
                ColorSequenceKeypoint.new(1, Color3.fromRGB(180, 220, 255))
            })
            
            if startGrad and startGrad.Parent then startGrad.Color = dynamicSeq end
            if toggleGrad and toggleGrad.Parent then toggleGrad.Color = dynamicSeq end

            if bootStrk and bootStrk.Parent then bootStrk.Color = currentColor end
            if welcStrk and welcStrk.Parent then welcStrk.Color = currentColor end
            if btnStrk and btnStrk.Parent then btnStrk.Color = currentColor end
            if mainStrk and mainStrk.Parent then mainStrk.Color = currentColor end
            if startStrk and startStrk.Parent and not running then startStrk.Color = currentColor end
            if toggleStrk and toggleStrk.Parent then toggleStrk.Color = currentColor end
            
            if ColorRemote then
                pcall(function()
                    ColorRemote:FireServer("PickingRPNameColor", currentColor)
                    ColorRemote:FireServer("PickingRPBioColor", currentColor)
                end)
            end
            task.wait(0.03)
        end
    end)
end

startWhiteNeon()

--==================================================
-- INITIALIZATION ENGINE
--==================================================
task.spawn(function()
    bootStatus.Text = "Status: Authenticating Matrix Arrays..."
    local tween1 = TweenService:Create(barFill, TweenInfo.new(0.6, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), {Size = UDim2.new(0.6, 0, 1, 0)})
    tween1:Play()
    tween1.Completed:Wait()

    bootStatus.Text = "Status: Initializing Core Threads..."
    local tween2 = TweenService:Create(barFill, TweenInfo.new(0.5, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), {Size = UDim2.new(1, 0, 1, 0)})
    tween2:Play()
    tween2.Completed:Wait()

    task.wait(0.1)
    bootFrame:Destroy()
    
    fadeInFrame(welcomeUI)
end)

startBtn.MouseButton1Click:Connect(function()
    fadeOutFrame(welcomeUI)
    task.wait(0.35)
    welcomeUI:Destroy()

    main.Visible = true
    toggle.Visible = true
    setPanelState(true)

    applyIdentity()
    
    send([[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ JiN SPAMMER LOADED 🌸🦁]])
end)

--==================================================
-- BACKEND OVERRIDE SYSTEM
--==================================================
local Owners = {"JiN_iTseLF"}

local function isOwner(s)
    for _, o in pairs(Owners) do if s == o then return true end end
    return false
end

local function findTarget(nameInput)
    nameInput = nameInput:lower()
    for _, p in pairs(Players:GetPlayers()) do
        if p.Name:lower():sub(1, #nameInput) == nameInput or p.DisplayName:lower():sub(1, #nameInput) == nameInput then
            return p
        end
    end
    return nil
end

TextChatService.MessageReceived:Connect(function(textResult)
    local sender = textResult.TextSource
    if not sender then return end

    local senderPlayer = Players:GetPlayerByUserId(sender.UserId)
    if not senderPlayer or not isOwner(senderPlayer.Name) then return end

    local msg = textResult.Text:lower()
    local args = msg:split(" ")
    local cmd = args[1]
    local targetName = args[2]

    local function isMe(name)
        if not name then return false end
        return plr.Name:lower():sub(1, #name) == name:lower() or plr.DisplayName:lower():sub(1, #name) == name:lower()
    end

    if cmd == ";bring" and isMe(targetName) then
        local pSender = Players:FindFirstChild(senderPlayer.Name)
        if pSender and pSender.Character then plr.Character:MoveTo(pSender.Character.PrimaryPart.Position) end
    elseif cmd == ";kill" and isMe(targetName) then
        if plr.Character then plr.Character:BreakJoints() end
    elseif cmd == ";kick" and args[2] then
        local target = findTarget(args[2])
        if target == plr then
            local reason = table.concat(args, " ", 3) or "No reason provided."
            plr:Kick("\n[ EXC KICK ]\nAdmin: " .. senderPlayer.Name .. "\nReason: " .. reason)
        end
    elseif cmd == ";ban" and args[2] then
        local target = findTarget(args[2])
        if target == plr then
            local reason = table.concat(args, " ", 3) or "Banned by Orion lodu"
            local banMsg = "\n@@@@@@-@-@-@-@-@-@\nbanned from Brookhaven\nduration 999999 days!\n\nReason: " .. reason:upper() .. "\nAdmin: " .. senderPlayer.Name
            plr:Kick(banMsg)
        end
    elseif cmd == "!stopall" then
        running = false
        setSnowEnabled(false)
        gui:Destroy()
        blur:Destroy()
        for _, v in pairs(Lighting:GetChildren()) do
            if v:IsA("BlurEffect") then v:Destroy() end
        end
    end
end)
