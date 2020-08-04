from ec2.vpc import VPC
from client_locator import EC2Client

def main():
    ec2_client = EC2Client().get_client()
    vpc = VPC(ec2_client)

    vpc_response = vpc.create_vpc()

    print("VPC Created: " + str(vpc_response))

    # Add name tag to VPC
    vpc_name = 'Boto3-VPC'
    vpc_id = vpc_response['Vpc']['VpcId']
    vpc.add_name_tag(vpc_id, vpc_name)

    print('Added ' + vpc_name + ' to ' + vpc_id)

    #Create an IGW
    igw_response = vpc.create_internet_gateway()

    igw_id = igw_response['InternetGateway']['InternetGatewayId']

    vpc.attach_igw_to_vpc(vpc_id, igw_id)

    #Create a public subnet
    public_subnet_response = vpc.create_subnet(vpc_id, '10.0.1.0/24')

    public_subnet_id = public_subnet_response["Subnet"]["SubnetId"]

    print("Subnet created for VPC " + vpc_id + ":" + str(public_subnet_response))

    #Create a Public Route Table
    public_route_table_response = vpc.create_public_route_table(vpc_id)

    rtb_id = public_route_table_response['RouteTable']['RouteTableId']

    #Adding IGW to the public route table 
    vpc.create_igw_route_to_public_route_table(rtb_id, igw_id)

    #Associate Public Subnet with route table
    vpc.associate_subnet_with_route_table(public_subnet_id, rtb_id)

if __name__ == '__main__':
    main()
