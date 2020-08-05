class VPC:
    def __init__(self, client):
        self._client = client
        """ :type : pyboto3.ec2"""

    def create_vpc(self):
        print("="*100)
        print("Creating a VPC.....")
        print("="*100)

        return self._client.create_vpc(
            CidrBlock = '10.0.0.0/16'
        )

    def add_name_tag(self, resource_id, resource_name):
        print("="*100)
        print("Adding " + resource_name + " tag to the " + resource_id)
        print("="*100)
        return self._client.create_tags(
            Resources = [resource_id],
            Tags = [{
                "Key" : "Name",
                "Value" : resource_name
            }]
        )

    def create_internet_gateway(self):
        print("Creating an Internet Gateway....")
        return self._client.create_internet_gateway()

    
    def attach_igw_to_vpc(self, vpc_id, igw_id):
        print("="*100)
        print("Attaching Internet Gateway " + igw_id + ' to VPC ' + vpc_id)
        print("="*100)
        return self._client.attach_internet_gateway(
            InternetGatewayId=igw_id,
            VpcId = vpc_id
        )

    def create_subnet(self, vpc_id, cidr_block):
        print("="*100)
        print("Creating a subnet for VPC" + vpc_id + " with CIDR block " + cidr_block)
        print("="*100)
        return self._client.create_subnet(
            VpcId = vpc_id,
            CidrBlock = cidr_block
        )

    def create_public_route_table(self, vpc_id):
        print("="*100)
        print("Creating public route table for VPC" + vpc_id)
        print("="*100)
        return self._client.create_route_table(VpcId = vpc_id)

    def create_igw_route_to_public_route_table(self, rtb_id, igw_id):
        print("="*100)
        print("Adding route for IGW" + igw_id + "To route table" + rtb_id)
        print("="*100)
        return self._client.create_route(
            RouteTableId = rtb_id,
            GatewayId = igw_id,
            DestinationCidrBlock = '0.0.0.0/0'
        )

    def associate_subnet_with_route_table(self, subnet_id, rtb_id):
        print("="*100)
        print("Associating subnet" + subnet_id + "With Route Table" + rtb_id)
        print("="*100)
        return self._client.associate_route_table(
            SubnetId = subnet_id,
            RouteTableId = rtb_id

        )

    def allow_auto_assign_ip_addresses_for_subnet(self, subnet_id):
        return self._client.modify_subnet_attribute(
            SubnetId = subnet_id,
            MapPublicIpOnLaunch = {'Value': True}
        )
