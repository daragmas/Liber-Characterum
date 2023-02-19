# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the bin/rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: "Star Wars" }, { name: "Lord of the Rings" }])
#   Character.create(name: "Luke", movie: movies.first)

require 'csv'

puts "Dropping Database..."

Trait.destroy_all
Armor.destroy_all
Skill.destroy_all
Passion.destroy_all
SpecialistSkill.destroy_all
Race.destroy_all

puts "Finished Dropping"

puts 'Starting Seed...'

puts "Seeding Traits..."

# csv_text = File.read('db/database_csvs/traits.csv')
csv = CSV.parse(File.read('db/database_csvs/traits.csv'), :headers =>true, :encoding => 'ISO-8859-1')

csv.each do |row|
    t = Trait.create!(name: row["Name"], description: row["Description"])
end

puts "Seeding Races..."

# csv_text = File.read('db/database_csvs/races.csv')
csv = CSV.parse(File.read('db/database_csvs/races.csv'), :headers =>true, :encoding => 'ISO-8859-1')

csv.each do |row|
    Race.create!(name: row['Name'], 
        starting_skills: row['Starting Skills'], 
        starting_specialist_skills: row['Starting Specialist Skills'],
        starting_skill_choices: row["Starting Skill Choices"],
        starting_talents: row["Starting Talents"],
        starting_traits: row["Starting Traits"],
        starting_armor: row["Starting Armor"],
        starting_equipment_choices: row["Starting Equipment Choices"],
        starting_gear: row["Starting Gear"],
        starting_xp: row["Starting XP"],
        description: row["Description"]
        )
end

puts "Seeding Skills"
csv = CSV.parse(File.read('db/database_csvs/skills.csv'), :headers =>true, :encoding => 'ISO-8859-1')

puts "Seeding Specialist Skills"
csv = CSV.parse(File.read('db/database_csvs/specialist_skills.csv'), :headers =>true, :encoding => 'ISO-8859-1')

puts "Seeding Armors"
csv = CSV.parse(File.read('db/database_csvs/armor.csv'), :headers =>true, :encoding => 'ISO-8859-1')

puts "Seeding Passions"
csv = CSV.parse(File.read('db/database_csvs/passions.csv'), :headers =>true, :encoding => 'ISO-8859-1')