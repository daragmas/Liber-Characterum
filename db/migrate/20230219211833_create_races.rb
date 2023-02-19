class CreateRaces < ActiveRecord::Migration[7.0]
  def change
    create_table :races do |t|
      t.string :name
      t.string :starting_skills
      t.string :starting_specialist_skills
      t.string :starting_skill_choices
      t.string :starting_talents
      t.string :starting_traits
      t.string :starting_armor
      t.string :starting_weapons
      t.string :starting_equipment_choices
      t.string :starting_gear
      t.integer :starting_xp
      t.string :description

      t.timestamps
    end
  end
end
