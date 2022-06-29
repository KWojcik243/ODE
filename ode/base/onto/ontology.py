from file import UserFile
from owlready2 import *
import types


# TODOO
# usunięcie wszystkich podklass
# delete_inverse_object_property nie działa
# data range nie działa

class ClassMan:
    def __init__(self, file: UserFile):
        self.file = file

    def create_subclass(self, subclass_name, main_class):
        with self.file.ontology:
            if main_class == "Thing":
                new_class = types.new_class(subclass_name, (eval(main_class),))
            else:
                new_class = types.new_class(subclass_name, (self.file.ontology[main_class],))

    def create_sibling_class(self, sibling_class_name, main_class):
        with self.file.ontology:
            new_class = types.new_class(sibling_class_name, (list(self.file.ontology[main_class].is_a)[0],))

    def delete_class(self, class_name, act_type):
        with self.file.ontology:
            match act_type:
                case "one":
                    if list(self.file.ontology[class_name].subclasses()):
                        for classes in list(self.file.ontology[class_name].subclasses()):
                            classes.is_a.append(list(self.file.ontology[class_name].is_a)[0])
                        destroy_entity(self.file.ontology[class_name])
                    else:
                        destroy_entity(self.file.ontology[class_name])
                case "all":
                    pass

    def add_subclass(self, subclass, main_class):
        with self.file.ontology:
            self.file.ontology[subclass].is_a.append(self.file.ontology[main_class])

    def delete_subclass(self, subclass, main_class):
        with self.file.ontology:
            self.file.ontology[main_class].is_a.remove(self.file.ontology[subclass])

    def add_equivalent_class(self, equclass, main_class):
        with self.file.ontology:
            self.file.ontology[equclass].equivalent_to.append(self.file.ontology[main_class])
            self.file.ontology[main_class].equivalent_to.append(self.file.ontology[equclass])

    def delete_equivalent_class(self, subclass, main_class):
        with self.file.ontology:
            self.file.ontology[main_class].equivalent_to.remove(self.file.ontology[subclass])
            self.file.ontology[subclass].equivalent_to.remove(self.file.ontology[main_class])

    # Instance


class InstancesMan:
    def __init__(self, file: UserFile):
        self.file = file

    def add_instance(self, which_class, name):
        with self.file.ontology:
            my_obj = self.file.ontology[which_class](name)
            my_obj.is_a.append(self.file.ontology[which_class])

    def delete_instance(self, which_class, name):
        with self.file.ontology:
            self.file.ontology[name].is_a.remove(self.file.ontology[which_class])

    def create_instance(self, which_class, name):
        with self.file.ontology:
            my_obj = self.file.ontology[which_class](name)

    def delete_instance_perm(self, name):
        with self.file.ontology:
            destroy_entity(self.file.ontology[name])

    def add_equivalent_instance(self, instance_1, instance_2):
        with self.file.ontology:
            self.file.ontology[instance_1].equivalent_to.append(self.file.ontology[instance_2])
            self.file.ontology[instance_2].equivalent_to.append(self.file.ontology[instance_1])

    def delete_equivalent_instance(self, instance_1, instance_2):
        with self.file.ontology:
            self.file.ontology[instance_1].equivalent_to.remove(self.file.ontology[instance_2])
            self.file.ontology[instance_2].equivalent_to.remove(self.file.ontology[instance_1])

    # Object property


class ObjectPropertyMan:
    def __init__(self, file: UserFile):
        self.file = file

    def create_object_sub_property(self, name, main_object_property):
        with self.file.ontology:
            if main_object_property == "ObjectProperty":
                new_class = types.new_class(name, (eval(main_object_property),))
            else:
                new_class = types.new_class(name, (self.file.ontology[main_object_property],))

    def create_sibling_object_property(self, name, main_object_property):
        with self.file.ontology:
            new_class = types.new_class(name, (list(self.file.ontology[main_object_property].is_a)[0],))

    def delete_object_property(self, object_property_name, act_type):
        with self.file.ontology:
            match act_type:
                case "one":
                    if list(self.file.ontology[object_property_name].subclasses()):
                        for classes in list(self.file.ontology[object_property_name].subclasses()):
                            classes.is_a.append(list(self.file.ontology[object_property_name].is_a)[0])
                        destroy_entity(self.file.ontology[object_property_name])
                    else:
                        destroy_entity(self.file.ontology[object_property_name])
                case "all":
                    pass

    def add_sub_property(self, sub_property, main_object_property):
        with self.file.ontology:
            self.file.ontology[sub_property].is_a.append(self.file.ontology[main_object_property])

    def delete_sub_property(self, sub_property, main_object_property):
        with self.file.ontology:
            self.file.ontology[main_object_property].is_a.remove(self.file.ontology[sub_property])

    def add_domain_object_property(self, domain, name):
        with self.file.ontology:
            self.file.ontology[name].domain.append(self.file.ontology[domain])

    def delete_domain_object_property(self, domain, name):
        with self.file.ontology:
            self.file.ontology[name].domain.remove(self.file.ontology[domain])

    def add_range_object_property(self, ob_range, name):
        with self.file.ontology:
            self.file.ontology[name].range.append(self.file.ontology[ob_range])

    def delete_range_object_property(self, ob_range, name):
        with self.file.ontology:
            self.file.ontology[name].range.remove(self.file.ontology[ob_range])

    def add_inverse_object_property(self, inverse_property, main_name):
        with self.file.ontology:
            self.file.ontology[main_name].inverse_property = self.file.ontology[inverse_property]
            self.file.ontology[inverse_property].inverse_property = self.file.ontology[main_name]

    def delete_inverse_object_property(self, inverse_property, main_name):
        with self.file.ontology:
            self.file.ontology[main_name].inverse_property = ""
            self.file.ontology[inverse_property].inverse_property = ""

    def add_equivalent_object_property(self, equclass, main_object_property):
        with self.file.ontology:
            self.file.ontology[equclass].equivalent_to.append(self.file.ontology[main_object_property])
            self.file.ontology[main_object_property].equivalent_to.append(self.file.ontology[equclass])

    def delete_equivalent_object_property(self, equclass, main_object_property):
        with self.file.ontology:
            self.file.ontology[equclass].equivalent_to.remove(self.file.ontology[main_object_property])
            self.file.ontology[main_object_property].equivalent_to.remove(self.file.ontology[equclass])

    # Data property


class DataPropertyMan:
    def __init__(self, file: UserFile):
        self.file = file

    def create_data_sub_property(self, name, main_data_property):
        with self.file.ontology:
            if main_data_property == "DataProperty":
                new_class = types.new_class(name, (eval(main_data_property),))
            else:
                new_class = types.new_class(name, (self.file.ontology[main_data_property],))

    def create_sibling_data_property(self, name, main_data_property):
        with self.file.ontology:
            new_class = types.new_class(name, (list(self.file.ontology[main_data_property].is_a)[0],))

    def delete_data_property(self, data_property_name, ac_type):
        with self.file.ontology:
            match ac_type:
                case "one":
                    if list(self.file.ontology[data_property_name].subclasses()):
                        for classes in list(self.file.ontology[data_property_name].subclasses()):
                            classes.is_a.append(list(self.file.ontology[data_property_name].is_a)[0])
                        destroy_entity(self.file.ontology[data_property_name])
                    else:
                        destroy_entity(self.file.ontology[data_property_name])
                case "all":
                    pass

    def add_sub_property(self, sub_property, main_data_property):
        with self.file.ontology:
            self.file.ontology[sub_property].is_a.append(self.file.ontology[main_data_property])

    def delete_sub_property(self, sub_property, main_data_property):
        with self.file.ontology:
            self.file.ontology[main_data_property].is_a.remove(self.file.ontology[sub_property])

    def add_domain_data_property(self, domain, name):
        with self.file.ontology:
            self.file.ontology[name].domain.append(self.file.ontology[domain])

    def delete_domain_data_property(self, domain, name):
        with self.file.ontology:
            self.file.ontology[name].domain.remove(self.file.ontology[domain])

    def add_range_data_property(self, range_data, name):
        with self.file.ontology:
            self.file.ontology[name].range.append(range_data)

    def delete_range_data_property(self, range_data, name):
        with self.file.ontology:
            self.file.ontology[name].range.remove(range_data)

    def add_equivalent_data_property(self, equdata, main_data_property):
        with self.file.ontology:
            self.file.ontology[equdata].equivalent_to.append(self.file.ontology[main_data_property])
            self.file.ontology[main_data_property].equivalent_to.append(self.file.ontology[equdata])

    def delete_equivalent_data_property(self, equdata, main_data_property):
        with self.file.ontology:
            self.file.ontology[equdata].equivalent_to.remove(self.file.ontology[main_data_property])
            self.file.ontology[main_data_property].equivalent_to.remove(self.file.ontology[equdata])

    def add_data_assertion(self, instance_name, main_data_property, value):
        with self.file.ontology:
            self.file.ontology[main_data_property].self.file.ontology[instance_name].append(value)

    def delete_data_assertion(self, instance_name, main_data_property, value):
        with self.file.ontology:
            self.file.ontology[main_data_property].self.file.ontology[instance_name].remove(value)
