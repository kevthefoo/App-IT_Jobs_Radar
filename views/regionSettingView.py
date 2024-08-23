import json, discord

from discord.ui import View 
from discord.ui import Button

class regionSettingView(View):
    def __init__(self, user, main_guild):
        self.user = user
        self.main_guild = main_guild
        super().__init__(timeout=None)
        with open('./data/views/regionSettingData.json', 'r') as f:
            data = json.load(f)

        for item in data:
            row= data.index(item)//5
            button = Button(label=item, custom_id=item, row=row)
            button.callback = self.buttonCallback
            self.add_item(button)

        for button in self.children:
            if button.label in [role.name for role in self.user.roles]:
                button.style = discord.ButtonStyle.green
            else:
                button.style = discord.ButtonStyle.gray

    async def buttonCallback(self, interaction: discord.Interaction):
        custom_id = interaction.data['custom_id']
        role = discord.utils.get(self.main_guild.roles , name=custom_id)
        all_buttons = self.children
        
        if role not in self.user.roles:
            for button in all_buttons:
                if button.label == custom_id:
                    button.style = discord.ButtonStyle.green
                    break

            await self.user.add_roles(role)
            await interaction.response.edit_message(content=f"**Select your regions**", view=self)
        else:
            for button in all_buttons:
                if button.label == custom_id:
                    button.style = discord.ButtonStyle.grey
                    break    
            await self.user.remove_roles(role)
            await interaction.response.edit_message(content=f"**Select your regions**", view=self)