class CreateSpecialistSkills < ActiveRecord::Migration[7.0]
  def change
    create_table :specialist_skills do |t|
      t.string  :name
      t.string  :characteristic
      t.string  :alignment
      t.string  :descriptors
      t.boolean    :trained_only
      t.timestamps
    end
  end
end
